#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8') # 进一步要求 python 使用 UTF-8

import numpy as np
import logging
import mxnet as mx

logging.getLogger().setLevel(logging.DEBUG)

batch_size = 100 # 在此增大了批大小，因为ResNet的训练较慢

# 残差模块
def ResBlock(net, suffix, n_block, n_filter, stride=(1,1)):
    for i in range(0, n_block):
        if i == 0: # 注意第1个残差层的定义不同，读者可观察结构图思考原因
            net = mx.sym.BatchNorm(net, name='bn'+suffix+'_a'+str(i), fix_gamma=False)
            net = mx.sym.Activation(net, name='act'+suffix+'_a'+str(i), act_type='relu')
            # 对于第1个残差层，旁路从此开始
            pathway = mx.sym.Convolution(net, name="adj"+suffix, kernel=(1,1), stride=stride, num_filter=n_filter)
            # 回到主路
            net = mx.sym.Convolution(net, name='conv'+suffix+'_a'+str(i), kernel=(3, 3), pad=(1, 1), num_filter = n_filter, stride=stride)
            net = mx.sym.BatchNorm(net, name='bn'+suffix+'_b'+str(i), fix_gamma=False)
            net = mx.sym.Activation(net, name='act'+suffix+'_b'+str(i), act_type='relu')
            net = mx.sym.Convolution(net, name='conv'+suffix+'_b'+str(i), kernel=(3, 3), pad=(1, 1), num_filter = n_filter)
            net = net + pathway # 加上旁路，即为残差结构
        else:
            pathway = net # 对于后续残差层，旁路从此开始
            net = mx.sym.BatchNorm(net, name='bn'+suffix+'_a'+str(i), fix_gamma=False)
            net = mx.sym.Activation(net, name='act'+suffix+'_a'+str(i), act_type='relu')
            net = mx.sym.Convolution(net, name='conv'+suffix+'_a'+str(i), kernel=(3, 3), pad=(1, 1), num_filter = n_filter)
            net = mx.sym.BatchNorm(net, name='bn'+suffix+'_b'+str(i), fix_gamma=False)
            net = mx.sym.Activation(net, name='act'+suffix+'_b'+str(i), act_type='relu')
            net = mx.sym.Convolution(net, name='conv'+suffix+'_b'+str(i), kernel=(3, 3), pad=(1, 1), num_filter = n_filter)
            net = net + pathway # 加上旁路，即为残差结构
    return net

net = mx.symbol.Variable('data')
# 为数据加上BN层可有一定的预处理效果
net = mx.sym.BatchNorm(net, name='bnPRE', fix_gamma=False)
# 将3*32*32变化为32*32*32
net = mx.sym.Convolution(net, name="convPRE", kernel=(3,3), pad=(1,1), num_filter=32)
# 将32*32*32变化为64*32*32
net = ResBlock(net, "1", 3, 64)
# 将64*32*32变化为64*16*16
net = ResBlock(net, "2", 3, 64, (2,2))
# 将64*16*16变化为128*8*8
net = ResBlock(net, "3", 3, 128, (2,2))
# 因为此前的最终层是卷积，因此再做BN和Act处理
net = mx.sym.BatchNorm(net, name='bnFINAL', fix_gamma=False)
net = mx.sym.Activation(net, name='actFINAL', act_type='relu')
# 将128*8*8变化为128*1*1
net = mx.sym.Pooling(net, name="pool", global_pool=True, pool_type="avg", kernel=(1,1))
# 将128*1*1变换为128
net = mx.sym.Flatten(net, name="flatten")
# 将128变换为10
net = mx.sym.FullyConnected(net, num_hidden=10, name='fc')
net = mx.sym.SoftmaxOutput(net, name='softmax')

# 输出参数情况供参考
shape = {"data" : (batch_size, 3, 28, 28)}
mx.viz.print_summary(symbol=net, shape=shape)

module = mx.mod.Module(symbol=net, context=mx.gpu(0)) # 网络模组

# 数据迭代器
train_iter = mx.io.ImageRecordIter(
            path_imgrec = "train.rec",
            data_shape  = (3,28,28), # 图像通道和尺寸
            batch_size  = batch_size,
            shuffle = True, # 开启随机次序
            rand_crop   = True, # 开启随机裁剪
            rand_mirror = True, # 开启随机镜像
            random_h = 10, # 随机色相
            random_s = 20, # 随机饱和度
            random_l = 25, # 随机亮度
            max_random_scale = 1.20, # 随机放大
            min_random_scale = 0.88, # 随机缩小 
            max_rotate_angle = 20, # 随机旋转
            max_aspect_ratio = 0.15, # 随机长宽比例
            max_shear_ratio = 0.10, # 随机倾斜比例
            fill_value = 0, # 四周填充黑色
) 
val_iter = mx.io.ImageRecordIter(
            path_imgrec = "test.rec",
            data_shape  = (3,28,28),
            batch_size  = batch_size,
            shuffle = False,
            rand_crop   = False,
            rand_mirror = False,
)

# 训练
module.fit(
    train_iter,
    eval_data=val_iter,
    initializer = mx.init.MSRAPrelu(slope=0.0), # 采用MSRAPrelu初始化
    optimizer = 'sgd', 
    # 采用0.5的初始学习速率，并在每50000个样本后将学习速率缩减为之前的0.984倍
    optimizer_params = {'learning_rate' : 0.5, 'lr_scheduler' : mx.lr_scheduler.FactorScheduler(step=50000/batch_size, factor=0.984)},
    num_epoch = 2,
    batch_end_callback = mx.callback.Speedometer(batch_size, 50000/batch_size)
)
