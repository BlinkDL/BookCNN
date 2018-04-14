#-*-coding:utf-8-*- # 如果使用py文件，需声明此文件为 UTF-8 格式，这样可以使用中文注释。如果使用ipynb文件，则无需此行

import mxnet as mx

# 每层的卷积神经元个数，AlphaGo Zero使用256个，我们为加快训练使用128个
n_filter = 128

net = mx.symbol.Variable('data')
# 预处理
net = mx.sym.Convolution(net, name='convPRE', kernel=(3, 3), pad=(1, 1), num_filter = n_filter)

# 残差结构
for i in range(0, 6):
    identity = net # 保存之前的输出
    net = mx.sym.BatchNorm(net, name='bnA'+str(i), fix_gamma=False)
    net = mx.sym.Activation(net, name='actA'+str(i), act_type='relu')
    net = mx.sym.Convolution(net, name='convA'+str(i), kernel=(3, 3), pad=(1, 1), num_filter = n_filter)
    net = mx.sym.BatchNorm(net, name='bnB'+str(i), fix_gamma=False)
    net = mx.sym.Activation(net, name='actB'+str(i), act_type='relu')
    net = mx.sym.Convolution(net, name='convB'+str(i), kernel=(3, 3), pad=(1, 1), num_filter = n_filter)
    net = net + identity # 直接加上之前的输出，即为残差结构

# 收尾工作
net = mx.sym.BatchNorm(net, name='bnFINAL', fix_gamma=False)
net = mx.sym.Activation(net, name='actFINAL', act_type='relu')
# 合并为1个通道
net = mx.sym.Convolution(net, name='convFINAL', kernel=(1, 1), num_filter=1)
net = mx.sym.Flatten(net)
# 输出为361个概率
net = mx.sym.SoftmaxOutput(net, name='softmax')

# 检查参数量
shape = {"data" : (32, 8, 19, 19)}
mx.viz.print_summary(symbol=net, shape=shape)
