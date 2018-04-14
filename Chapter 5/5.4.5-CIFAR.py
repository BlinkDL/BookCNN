#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8') # 进一步要求 python 使用 UTF-8

import numpy as np
import logging
import mxnet as mx

logging.getLogger().setLevel(logging.DEBUG)

batch_size = 50 # 批大小

# 用于辅助定义网络，这是深度卷积网络中很常用的"Conv-BN-Act"模块
def CBA(src, suffix, num_filter, kernel, pad, stride=(1,1)):
    conv = mx.sym.Convolution(src, name="conv"+suffix, kernel=(kernel,kernel), pad=(pad,pad), num_filter=num_filter, stride=stride)
    bn = mx.sym.BatchNorm(conv, name="bn"+suffix, fix_gamma=False)
    act = mx.sym.Activation(bn, name="act"+suffix, act_type="relu")
    return act

# 全卷积架构，由带步长的卷积实现缩小
net = mx.symbol.Variable('data')
# 将3*28*28变换为96*28*28
net = CBA(net, "1", 96, 3, 1)
# 将96*28*28变换为96*28*28
net = CBA(net, "2", 96, 3, 1)
# 将96*28*28变换为96*14*14
net = CBA(net, "3", 96, 3, 1, (2,2))
# 将96*14*14变换为192*14*14
net = CBA(net, "4", 192, 3, 1)
# 将192*14*14变换为192*14*14
net = CBA(net, "5", 192, 3, 1)
# 将192*14*14变换为192*7*7
net = CBA(net, "6", 192, 3, 1, (2,2))
# 将192*7*7变换为192*5*5
net = CBA(net, "7", 192, 3, 0)
# 将192*5*5变换为192*5*5
net = CBA(net, "8", 192, 1, 0)
# 将192*5*5变换为10*5*5
net = CBA(net, "9", 10, 1, 0)
# 将10*5*5变换为10*1*1
net = mx.sym.Pooling(net, name="pool", global_pool=True, pool_type="avg", kernel=(1,1))
# 将10*1*1变换为10
net = mx.sym.Flatten(net, name="flatten")
net = mx.sym.SoftmaxOutput(net, name='softmax')
 
# 输出参数情况供参考
shape = {"data" : (batch_size, 3, 28, 28)}
mx.viz.print_summary(symbol=net, shape=shape)

# 由于训练数据多，这里采用了GPU，若读者没有GPU，可修改为CPU
module = mx.mod.Module(symbol=net, context=mx.gpu(0))

# 迭代器，训练数据：
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
# 测试数据，关闭数据增强： 
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
# 采用0.5的初始学习速率，并在每50000个样本后将学习速率缩减为之前的0.98倍
    optimizer_params = {'learning_rate' : 0.5, 'lr_scheduler' : mx.lr_scheduler.FactorScheduler(step=50000/batch_size, factor=0.98)},
    num_epoch = 200,
    batch_end_callback = mx.callback.Speedometer(batch_size, 50000/batch_size)
)
