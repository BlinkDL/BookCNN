#-*-coding:utf-8-*-
import numpy as np
import os
import gc
import time
import struct
import sys
import multiprocessing
import random
import mxnet as mx
from mxnet.ndarray import concatenate
from mxnet.io import DataIter, DataDesc
from collections import OrderedDict, namedtuple

# 载入自定义的辅助库
import config
import symmetry
from utils import MyNetwork, my_print

# 定义需监控的性能指标
my_metric = [mx.metric.create('acc'), # 准确率
             mx.metric.create('ce'), # 交叉熵损失
             mx.metric.create('top_k_accuracy', top_k = 2), # 前2位命中率
             mx.metric.create('top_k_accuracy', top_k = 5), # 前5位命中率
             mx.metric.create('top_k_accuracy', top_k = 10)] # 前10位命中率

# 储存部分指标
epoch_accuracy = 0
epoch_loss = 0
epoch_loss_last = -1
time_last = None # 监控训练耗时

# 主函数

def main(argv):

    # 定义网络
    net = mx.sym.Variable('data')
    
    net = MyNetwork().MyBlocks(data=net, blocks=1, block_type="C", name="pre", n_filter=128, kernel=3)
    net = MyNetwork().MyBlocks(data=net, blocks=6, block_type="R-BACBAC", name="", n_filter=128, kernel=3)
    net = MyNetwork().MyBlocks(data=net, blocks=1, block_type="BAC", name="final", n_filter=1, kernel=1)
    
#    net = MyNetwork().MyBlocks(data=net, blocks=1, block_type="C", name="pre", n_filter=1, kernel=3)
    
    net = mx.sym.Flatten(data=net)
    net = mx.sym.SoftmaxOutput(data=net, name='softmax')
    # 输出参数情况
    shape = {"data" : (1, 8, 19, 19)}
    mx.viz.print_summary(symbol=net, shape=shape)

    # 建立输出模型目录
    if not os.path.exists(config.model_directory):
        os.mkdir(config.model_directory)
    # 建立日志文件
    log_file = os.open(config.model_directory + "//_train_.csv", os.O_RDWR|os.O_CREAT|os.O_APPEND)

    # 新建模型，或载入此前的模型
    if config.n_epoch_load == 0:
        module = mx.mod.Module(symbol=net, context=config.train_device)
        arg_params = None
        aux_params = None
    else:
        sym, arg_params, aux_params = mx.model.load_checkpoint(config.model_prefix, config.n_epoch_load)
        module = mx.mod.Module(symbol=sym, context=config.train_device)

    # 建立迭代器，这里最后一个参数代表是否是用于训练（训练时需进行数据增强，测试时不需要）
    data_iter = MyDataIter(config.batch_size, True)
    val_iter = MyDataIter(config.batch_size, False)
    
    # 如前所述，我们将棋谱数据分为多个文件，这里定义每完成1个文件为1个虚拟epoch
    def epoch_callback(epoch, symbol, arg_params, aux_params):
        global time_last, epoch_accuracy, epoch_loss, epoch_loss_last
        
        # 输出真正的epoch数（每完成1次全部文件的训练，为一个真正的epoch）
        real_epoch = float(epoch) / (config.train_end_index - config.train_begin_index + 1)
        my_print(' %.2f', (real_epoch))

        # 输出性能指标
        batch_accuracy = my_metric[0].get_name_value()[0][1]
        cross_loss = my_metric[1].get_name_value()[0][1];
        my_print(' : 1/2/5/10 %.2f', (100.0 * batch_accuracy))
        my_print('-%.2f', (100.0 * my_metric[2].get_name_value()[0][1]))
        my_print('-%.2f', (100.0 * my_metric[3].get_name_value()[0][1]))
        my_print('-%.2f%%', (100.0 * my_metric[4].get_name_value()[0][1]))
        my_print(' ce %.3f', (cross_loss))
        # 输出当前学习速率
        my_print(' : lr %.4f' % (config.learning_rate))

        # 更新一些性能指标
        epoch_accuracy += batch_accuracy;
        epoch_loss += cross_loss;

        # 输出训练耗时
        time_now = time.time()
        if time_last is None:
            time_last = time_now
            my_print(' : n/a\n')
        else:
            my_print(' : %.2fs\n' % (time_now - time_last))
        time_last = time_now

        # 定期保存模型，并测试性能，并调整学习速率
        if epoch % config.save_period == 0:
            # 保存模型
            module.save_checkpoint(config.model_prefix, epoch, save_optimizer_states=True)
            
            # 测试在测试数据集的性能指标
            val_metric = module.score(val_iter, [mx.metric.Accuracy(), mx.metric.CrossEntropy()])
            val_accuracy = val_metric[0][1]
            val_loss = val_metric[1][1]
            # 输出性能指标
            epoch_accuracy = float(epoch_accuracy) / config.save_period
            epoch_loss = float(epoch_loss) / config.save_period
            print("=== [saved] : train %.2f%% ce %.3f : validate %.2f%% ce %.3f ===" % 
                  (100.0 * epoch_accuracy,
                   epoch_loss,
                   100.0 * val_accuracy,
                   val_loss))
            # 保存到日志中
            os.write(log_file, str(real_epoch) + "," + str(epoch_accuracy) + "," + str(val_accuracy) + "," + str(config.learning_rate) + "\n")
            os.fsync(log_file)

            # 自适应地减少学习速率：如果在训练数据的平均损失提高了，则减少学习速率
            if epoch_loss > epoch_loss_last and epoch_loss_last != -1:
                config.learning_rate = config.learning_rate * config.learning_decay
            epoch_loss_last = epoch_loss
            epoch_accuracy = 0.0
            epoch_loss = 0.0
            # 学习速率很低时，终止训练
            if config.learning_rate < config.exit_learning_rate:
                exit(0)
    
    def batch_callback(epoch):
        data_iter.can_load_file.set() # 训练开始，发送信号表示CPU可接着加载后续的文件

    # 开始训练
    module.fit(
        data_iter,
        eval_data = None, # 我们会自行测试
        eval_metric = my_metric,
        initializer = mx.initializer.MSRAPrelu(factor_type='avg', slope=0.0),

        optimizer = 'sgd',
        optimizer_params = {'learning_rate': config.learning_rate, 'wd': config.wd, 'momentum': 0},
        
        num_epoch = 9999999, # 我们会自行决定何时终止训练
        batch_end_callback = batch_callback,
        epoch_end_callback = epoch_callback,
        arg_params = arg_params,
        aux_params = aux_params,
        begin_epoch = config.n_epoch_load + 1 # 延续之前的训练进度
    )


# 与我们自定义的数据迭代器有关         
class OneBatch(object):
    def __init__(self, data, label, pad=None, index=None,
                 bucket_key=None, provide_data=None, provide_label=None):
        self.data = data
        self.label = label
        self.pad = pad
        self.index = index
        self.bucket_key = bucket_key
        self.provide_data = provide_data
        self.provide_label = provide_label

# 我们自定义的数据迭代器
class MyDataIter(DataIter):
    
    # 负责载入文件
    def load_file(self):
        while True: # 是一个死循环，但会等待信号，因此不会卡死
            filename = ""
            
            # 获取需载入的文件名
            if self.is_train:
                index = self.train_list[self.train_index]
                my_print('[pl %s' % str(index).rjust(4))
                filename = config.train_prefix + '-' + str(index) + '.dat'
            else:
                filename = config.train_prefix + "-val.dat"
                my_print('[pl validate data')
            
            # 载入数据文件
            with open(filename, 'rb') as data_file:
                data = bytearray(data_file.read())
            
            # 加入随机变换
            if self.is_train and config.apply_symmetry:
                symmetry.apply_random_symmetry(data)
                
            # 将读入的文件设置为正确的数组格式
            data = np.array(data).reshape(-1, config.head+361)
            
            # 打散数据
            if self.is_train and config.shuffle_data:
                np.random.shuffle(data)
            
            # 将落子位置由XY坐标变为0-360的数
            label = np.array(map(lambda x, y : x + y * 19, \
                                data[:, 0:1].flatten(), data[:, 1:2].flatten()), \
                                np.uint16)

            # 获取特征层，设置为正确的数组格式
            data = np.unpackbits(data[:, config.head:config.head+361]).reshape(-1, 19, 19, 8)
            data = np.moveaxis(data, -1, 1)
            
            # 载入完成
            my_print(']')

            if self.is_train: # 如果是载入训练数据，则需要不断载入
                # 将数据填充到队列中
                self.queue.put(obj = [data, label], block = True, timeout = None) # save                 
                self.train_index = self.train_index + 1
                # 如已完成全部文件的训练，则重新打散文件的顺序
                if (self.train_index >= len(self.train_list)):
                    self.train_index = 0
                    random.shuffle(self.train_list)
            else: # 如果是载入测试数据，则可一次载入
                self.data_list = [mx.ndarray.array(data, config.data_device), mx.ndarray.array(label, config.data_device)]
                
            gc.collect() # 要求垃圾回收，否则会耗费大量内存
                
            if not self.is_train:
                return # 如果是载入测试数据，则一次就已完成载入
                            
            # 否则会停下来等待信号
            if self.is_train:
                self.can_load_file.wait()
                self.can_load_file.clear()

    # 负责加载数据
    def init_data(self):            
        if self.is_train: 
            tmp = self.queue.get(block = True, timeout = None) # 从队列加载数据
            self.data_list = [mx.ndarray.array(tmp[0], config.data_device), mx.ndarray.array(tmp[1], config.data_device)]

        # 按MXNet所要求的规范设置
        self.data = [('data', self.data_list[0])]
        self.label = [('softmax_label', self.data_list[1])]
        # 设置数据个数
        self.num_data = self.data_list[0].shape[0]
        assert self.num_data >= self.batch_size, "batch_size need to be smaller than data size."

    # 负责初始化迭代器
    def __init__(self, batch_size=1, is_train = True):
        super(MyDataIter, self).__init__()
        
        self.can_load_file = multiprocessing.Event()

        self.cursor = -batch_size
        self.batch_size = batch_size
        
        # 打散加载文件的列表
        self.train_index = 0        
        self.train_list = range(config.train_begin_index, config.train_end_index+1)
        random.shuffle(self.train_list)
        
        self.is_train = is_train        
        if self.is_train: # 如果是训练数据，则开启队列和加载数据的线程
            if __name__ == '__main__':
                self.queue = multiprocessing.Queue(maxsize = 1)
                self.worker = multiprocessing.Process(target = self.load_file)
                self.worker.daemon = True
                self.worker.start()
                self.init_data()
                self.init_misc()
        else: # 如果是测试数据，则直接加载数据
            self.load_file()
            self.init_data()
            self.init_misc()

    # 下面是一些细节函数，基本来自于MXNet源代码中迭代器的定义的复制粘贴，毋需特别关注
    def init_misc(self):  
        self.num_source = len(self.data_list)
        self.provide_data = [ DataDesc(k, tuple([self.batch_size] + list(v.shape[1:])), v.dtype)
            for k, v in self.data ] 
        self.provide_label = [ DataDesc(k, tuple([self.batch_size] + list(v.shape[1:])), v.dtype)
            for k, v in self.label ]

    def hard_reset(self):
        self.cursor = -self.batch_size

    def reset(self):
        if self.is_train: 
            self.init_data()
        self.cursor = -self.batch_size

    def next(self):
        self.cursor += self.batch_size
        if self.cursor < self.num_data:
            return OneBatch(data=self.getdata(), label=self.getlabel(), pad=self.getpad(), index=None)
        else:
            raise StopIteration

    def _getdata(self, data_source):
        if self.cursor + self.batch_size <= self.num_data: # no pad
            return [x[1][self.cursor:self.cursor+self.batch_size] for x in data_source]
        else: # with pad
            pad = self.batch_size - self.num_data + self.cursor
            return [concatenate([x[1][self.cursor:], x[1][:pad]]) for x in data_source]

    def getdata(self):
        return self._getdata(self.data)

    def getlabel(self):
        return self._getdata(self.label)

    def getpad(self):
        if self.cursor + self.batch_size > self.num_data:
            return self.cursor + self.batch_size - self.num_data
        else:
            return 0        
        
# 运行主函数
if __name__ == '__main__':
    main(sys.argv)
