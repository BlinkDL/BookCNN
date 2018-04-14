#-*-coding:utf-8-*- # 如果使用py文件，需声明此文件为 UTF-8 格式，这样可以使用中文注释。如果使用ipynb文件，则无需此行
import sys
reload(sys)
sys.setdefaultencoding('utf-8') # 进一步要求 python 使用 UTF-8

import numpy as np
import os
import gzip
import struct
import logging
import mxnet as mx
import matplotlib.pyplot as plt # 这是常用的绘图库

logging.getLogger().setLevel(logging.DEBUG)

def read_data(label_url, image_url): # 读入训练数据
    with gzip.open(label_url) as flbl: # 打开标签文件
        magic, num = struct.unpack(">II", flbl.read(8)) # 读入标签文件头
        label = np.fromstring(flbl.read(), dtype=np.int8) # 读入标签内容
    with gzip.open(image_url, 'rb') as fimg: # 打开图像文件
        magic, num, rows, cols = struct.unpack(">IIII", fimg.read(16)) # 读入图像文件头
        image = np.fromstring(fimg.read(), dtype=np.uint8) # 读入图像内容
        image = image.reshape(len(label), 1, rows, cols) # 设置为正确的数组格式
        image = image.astype(np.float32)/255.0 # 归一化到0到1区间
    return (label, image)

# 读入数据
(train_lbl, train_img) = read_data('train-labels-idx1-ubyte.gz', 'train-images-idx3-ubyte.gz')
(val_lbl, val_img) = read_data('t10k-labels-idx1-ubyte.gz', 't10k-images-idx3-ubyte.gz')

batch_size = 32 # 批大小

# 迭代器
train_iter = mx.io.NDArrayIter(train_img, train_lbl, batch_size, shuffle=True)
val_iter = mx.io.NDArrayIter(val_img, val_lbl, batch_size) 

# 设置网络
data = mx.symbol.Variable('data')

# 将图像摊平，例如1*28*28的图像就变为784个数据点，这样才可与普通神经元连接
flatten = mx.sym.Flatten(data=data, name="flatten")

# 第1层网络及非线性激活
fc1  = mx.sym.FullyConnected(data=flatten, num_hidden=128, name="fc1")
act1 = mx.sym.Activation(data=fc1, act_type="relu", name="act1")

# 第2层网络及非线性激活
fc2  = mx.sym.FullyConnected(data=act1, num_hidden=64, name="fc2")
act2 = mx.sym.Activation(data=fc2, act_type="relu", name="act2")
    
# 输出神经元，因为需分为10类，所以有10个神经元
fc3  = mx.sym.FullyConnected(data=act2, num_hidden=10, name="fc3")
# SoftMax
net  = mx.sym.SoftmaxOutput(data=fc3, name='softmax')

shape = {"data" : (batch_size, 1, 28, 28)}
mx.viz.print_summary(symbol=net, shape=shape)


# 由于训练数据量较大，这里采用了GPU，若读者没有GPU，可修改为CPU
module = mx.mod.Module(symbol=net, context=mx.gpu(0))

module.fit(
    train_iter,
    eval_data=val_iter,
    optimizer = 'sgd',
# 采用0.2的初始学习速率，并在每60000个样本后（即每1个epoch后）将学习速率缩减为之前的0.9倍
    optimizer_params = {'learning_rate' : 0.2, 'lr_scheduler' : mx.lr_scheduler.FactorScheduler(step=60000/batch_size, factor=0.9)},
    num_epoch = 20,
    batch_end_callback = mx.callback.Speedometer(batch_size, 60000/batch_size)
)
