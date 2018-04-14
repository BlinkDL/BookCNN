#-*-coding:utf-8-*-

import logging
import math
import random
import mxnet as mx # 导入 MXNet 库
import numpy as np # 导入 NumPy 库，这是 Python 常用的科学计算库

n_sample = 2 # 训练用的样本个数
batch_size = 1 # 批大小
learning_rate = 0.1 # 学习速率
n_epoch = 1 # 训练 epoch 数

train_in = [[0.5, 1], [0.2, 0.6]] # 为测试，设置2个固定样本 
train_out = [1, 0.6] # 设置相应的训练目标

# 为测试，关闭了随机顺序
train_iter = mx.io.NDArrayIter(data = np.array(train_in), label = {'reg_label':np.array(train_out)}, batch_size = batch_size, shuffle = False)

src = mx.sym.Variable('data') # 输入层
fc1  = mx.sym.FullyConnected(data = src, num_hidden = 2, name = 'fc1') # 全连接层
act1 = mx.sym.Activation(data = fc1, act_type = "relu", name = 'act1') # ReLU层
fc2  = mx.sym.FullyConnected(data = act1, num_hidden = 1, name = 'fc2') # 全连接层
net = mx.sym.LinearRegressionOutput(data = fc2, name = 'reg') # 输出层

# 定义模组
mod = mx.mod.Module(symbol = net, label_names = (['reg_label']))
# 需手动绑定训练数据和标签
mod.bind(data_shapes=train_iter.provide_data, label_shapes=train_iter.provide_label)
# 为测试，采用纯手动初始化：
mod.init_params(arg_params={
    'fc1_weight':mx.nd.array([[0.5, 0], [0.5, 1]]),
    'fc1_bias':mx.nd.array([0, 0]),
    'fc2_weight':mx.nd.array([[0.5, 0.5]]),
    'fc2_bias':mx.nd.array([0])
})
# 正常情况下，可用MXNet的自带函数初始化，例如：
# mod.init_params(initializer=mx.init.Uniform(scale=0.1))

# 设置优化器
mod.init_optimizer(optimizer='sgd', optimizer_params=(('learning_rate', 0.1), ))
# 设置需跟踪的性能指标
metric = mx.metric.create('mse')

for epoch in range(1): # 手动训练，这里只训练1个epoch
    train_iter.reset() # 每个epoch需手动将迭代器复位
    # 实际训练时，应在此调用 metric.reset() 将性能指标复位
    for batch in train_iter: # 对于每个batch...
        print('============ input ============')
        print(batch.data) # 数据
        print(batch.label) # 数据的标签
        mod.forward(batch, is_train=True) # 前向传播
        print('============ output ============')
        print(mod.get_outputs()) # 网络的输出
        metric.reset() # 这里希望看网络的训练细节，所以对于每个样本都将指标复位
        mod.update_metric(metric, batch.label) # 更新指标
        print('============ metric ============')
        print(metric.get()) # 指标的情况
        mod.backward() # 反向传播，计算梯度
        print('============ grads ============')
        print(mod._exec_group.grad_arrays) # 输出梯度情况
        mod.update() # 根据梯度情况，由优化器更新网络参数
        print('============ params ============')
        print(mod.get_params()) # 输出新的参数
        print('\n')
