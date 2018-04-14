#-*-coding:utf-8-*- # 如果使用py文件，需声明此文件为 UTF-8 格式，这样可以使用中文注释。如果使用ipynb文件，则无需此行

import mxnet as mx

########### 在AlphaGo v13和v18中的策略网络和价值网络 ###########

n_filter = 192 #每层的卷积神经元个数

pnet = mx.symbol.Variable('data') #策略网络
for i in range(1, 12+1): #构建第1-12层
    if i == 1: #第1层是5*5卷积
        pnet = mx.sym.Convolution(pnet, name='conv'+str(i), kernel=(5, 5), pad=(2, 2), num_filter = n_filter)
    else: #第2-12层是3*3卷积
        pnet = mx.sym.Convolution(pnet, name='conv'+str(i), kernel=(3, 3), pad=(1, 1), num_filter = n_filter)
    pnet = mx.sym.Activation(pnet, name='act'+str(i), act_type='relu')
    
#合并为1个通道
pnet = mx.sym.Convolution(pnet, name='convFINAL', kernel=(1, 1), num_filter=1)
pnet = mx.sym.Flatten(pnet)
#输出为361个概率
pnet = mx.sym.SoftmaxOutput(pnet, name='softmax')

vnet = mx.symbol.Variable('data') #价值网络
for i in range(1, 13+1): #构建第1-13层
    if i == 1: #第1层是5*5卷积
        vnet = mx.sym.Convolution(vnet, name='conv'+str(i), kernel=(5, 5), pad=(2, 2), num_filter = n_filter)
    elif i < 13: #第2-12层是3*3卷积
        vnet = mx.sym.Convolution(vnet, name='conv'+str(i), kernel=(3, 3), pad=(1, 1), num_filter = n_filter)
    elif i == 13: #第13层是1*1卷积
        vnet = mx.sym.Convolution(vnet, name='conv'+str(i), kernel=(1, 1), num_filter = 1)
    vnet = mx.sym.Activation(vnet, name='act'+str(i), act_type='relu')
#全连接层
vnet = mx.sym.Flatten(vnet)
vnet = mx.sym.FullyConnected(data=vnet, name='fc1', num_hidden=256)
vnet = mx.sym.Activation(vnet, name='fc1_act', act_type='relu')
#输出为1个概率
vnet  = mx.sym.FullyConnected(data=vnet, name='fc2', num_hidden=1)
vnet = mx.sym.LogisticRegressionOutput(data=vnet, name='out')

#检查参数量和结构图
shape = {"data" : (128, 48, 19, 19)}
mx.viz.print_summary(symbol=pnet, shape=shape)
shape = {"data" : (128, 49, 19, 19)}
mx.viz.print_summary(symbol=vnet, shape=shape)

########### 在AlphaGo Zero中的综合网络 ###########

n_filter = 256 #每层的卷积神经元个数
n_blocks = 39 #残差单元数

#初始卷积单元
net = mx.symbol.Variable('data')
net = mx.sym.Convolution(net, name='convPRE', kernel=(3, 3), pad=(1, 1), num_filter = n_filter)
net = mx.sym.BatchNorm(net, name='bnPRE', fix_gamma=False)
net = mx.sym.Activation(net, name='actPRE', act_type='relu')

for i in range(1, n_blocks+1): #残差单元
    identity = net # 保存之前的输出
    net = mx.sym.Convolution(net, name='convA'+str(i), kernel=(3, 3), pad=(1, 1), num_filter = n_filter)
    net = mx.sym.BatchNorm(net, name='bnA'+str(i), fix_gamma=False)
    net = mx.sym.Activation(net, name='actA'+str(i), act_type='relu')
    net = mx.sym.Convolution(net, name='convB'+str(i), kernel=(3, 3), pad=(1, 1), num_filter = n_filter)
    net = mx.sym.BatchNorm(net, name='bnB'+str(i), fix_gamma=False)
    net = net + identity # 加上之前的输出，即为残差结构
    net = mx.sym.Activation(net, name='actB'+str(i), act_type='relu')

#策略输出
pnet = mx.sym.Convolution(net, name='convP', kernel=(1, 1), num_filter=2)
pnet = mx.sym.BatchNorm(pnet, name='bnP', fix_gamma=False)
pnet = mx.sym.Activation(pnet, name='actP', act_type='relu')
pnet = mx.sym.Flatten(pnet)
#输出为362个概率，对应361个着点，或停一手（代表棋局结束）
pnet = mx.sym.FullyConnected(data=pnet, name='fcP', num_hidden=362)
pnet = mx.sym.SoftmaxOutput(pnet, name='softmaxP')

#价值输出
vnet = mx.sym.Convolution(net, name='convV', kernel=(1, 1), num_filter=1)
vnet = mx.sym.BatchNorm(vnet, name='bnV', fix_gamma=False)
vnet = mx.sym.Activation(vnet, name='actV', act_type='relu')
vnet = mx.sym.Flatten(vnet)
#全连接层
vnet = mx.sym.FullyConnected(data=vnet, name='fc1V', num_hidden=256)
vnet = mx.sym.Activation(vnet, name='fc1_actV', act_type='relu')
vnet = mx.sym.FullyConnected(data=vnet, name='fc2V', num_hidden=1)
vnet = mx.sym.LogisticRegressionOutput(data=vnet, name='outV')

#检查参数量和结构图
shape = {"data" : (32, 17, 19, 19)}
mx.viz.print_summary(symbol=pnet, shape=shape)
mx.viz.print_summary(symbol=vnet, shape=shape)
