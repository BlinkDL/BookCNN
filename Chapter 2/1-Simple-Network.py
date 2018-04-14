#-*-coding:utf-8-*- # 如果使用py文件，需声明此文件为 UTF-8 格式，这样可以使用中文注释。如果使用ipynb文件，则无需此行

import logging
import math
import random
import mxnet as mx # 导入 MXNet 库
import numpy as np # 导入 NumPy 库，这是 Python 常用的科学计算库

logging.getLogger().setLevel(logging.DEBUG) # 打开调试信息的显示

n_sample = 10000 # 训练用的数据点个数
batch_size = 10 # 批大小
learning_rate = 0.1 # 学习速率
n_epoch = 10 # 训练 epoch 数

# 每个数据点是在 (0,1) 之间的 2 个随机数
train_in = [[ random.uniform(0, 1) for c in range(2)] for n in range(n_sample)] 

train_out = [0 for n in range(n_sample)] # 期望输出，先初始化为 0

for i in range(n_sample):
    # 每个数据点的期望输出是 2 个输入数中的大者
    train_out[i] = max(train_in[i][0], train_in[i][1])

train_iter = mx.io.NDArrayIter(data = np.array(train_in), label = {'reg_label':np.array(train_out)}, batch_size = batch_size, shuffle = True)

src = mx.sym.Variable('data') # 输入层
fc1  = mx.sym.FullyConnected(data = src, num_hidden = 10, name = 'fc1') # 全连接层
act1 = mx.sym.Activation(data = fc1, act_type = "relu", name = 'act1') # ReLU层
fc2  = mx.sym.FullyConnected(data = act1, num_hidden = 10, name = 'fc2') # 全连接层
act2 = mx.sym.Activation(data = fc2, act_type = "relu", name = 'act2') # ReLU层
fc3  = mx.sym.FullyConnected(data = act2, num_hidden = 1, name = 'fc3') # 全连接层
net = mx.sym.LinearRegressionOutput(data = fc3, name = 'reg') # 输出层

module = mx.mod.Module(symbol = net, label_names = (['reg_label']))

module.fit(
    train_iter, # 训练数据的迭代器
    eval_data = None, # 在此只训练，不使用测试数据
    eval_metric = mx.metric.create('mse'), # 输出 MSE 损失信息
    # 将权重和偏置初始化为在[-0.5, 0.5]间均匀的随机数 
    initializer = mx.initializer.Uniform(0.5), 
    optimizer = 'sgd', # 梯度下降算法为 SGD
    # 设置学习速率
    optimizer_params = {'learning_rate': learning_rate}, 
    num_epoch = n_epoch, # 训练 epoch 数
    batch_end_callback = None, # 减少输出信息
    epoch_end_callback = None # 减少输出信息
)

for k in module.get_params(): # 对于所有参数…
    print(k) # 输出参数
