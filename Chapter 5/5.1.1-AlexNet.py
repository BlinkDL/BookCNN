#-*-coding:utf-8-*- # 如果使用py文件，需声明此文件为 UTF-8 格式，这样可以使用中文注释。如果使用ipynb文件，则无需此行

import mxnet as mx

data = mx.symbol.Variable('data')
# 3*224*224 => 96*54*54
conv1 = mx.sym.Convolution(name='conv1', data=data, kernel=(11, 11), stride=(4, 4), num_filter=96)
relu1 = mx.sym.Activation(data=conv1, act_type="relu")
# 96*54*54 => 96*26*26
pool1 = mx.sym.Pooling(data=relu1, pool_type="max", kernel=(3, 3), stride=(2,2))
# 96*26*26 => 256*26*26
conv2 = mx.sym.Convolution(name='conv2', data=pool1, kernel=(5, 5), pad=(2, 2), num_filter=256)
relu2 = mx.sym.Activation(data=conv2, act_type="relu")
# 256*26*26 => 256*12*12
pool2 = mx.sym.Pooling(data=relu2, kernel=(3, 3), stride=(2, 2), pool_type="max")
# 256*12*12 => 384*12*12
conv3 = mx.sym.Convolution(name='conv3', data=pool2, kernel=(3, 3), pad=(1, 1), num_filter=384)
relu3 = mx.sym.Activation(data=conv3, act_type="relu")
# 384*12*12 => 384*12*12
conv4 = mx.sym.Convolution(name='conv4',data=relu3, kernel=(3, 3), pad=(1, 1), num_filter=384)
relu4 = mx.sym.Activation(data=conv4, act_type="relu")
# 384*12*12 => 256*12*12
conv5 = mx.sym.Convolution(name='conv5', data=relu4, kernel=(3, 3), pad=(1, 1), num_filter=256)
relu5 = mx.sym.Activation(data=conv5, act_type="relu")
# 256*12*12 => 256*5*5
pool3 = mx.sym.Pooling(data=relu5, kernel=(3, 3), stride=(2, 2), pool_type="max")
# 256*5*5 => 6400
flatten = mx.sym.Flatten(data=pool3)
# 6400 => 4096
fc1 = mx.sym.FullyConnected(name='fc1', data=flatten, num_hidden=4096)
relu6 = mx.sym.Activation(data=fc1, act_type="relu")
dropout1 = mx.sym.Dropout(data=relu6, p=0.5)
# 4096 => 4096
fc2 = mx.sym.FullyConnected(name='fc2', data=dropout1, num_hidden=4096)
relu7 = mx.sym.Activation(data=fc2, act_type="relu")
dropout2 = mx.sym.Dropout(data=relu7, p=0.5)
# 4096 => 1000
fc3 = mx.sym.FullyConnected(name='fc3', data=dropout2, num_hidden=1000)
softmax = mx.sym.SoftmaxOutput(data=fc3, name='softmax')

shape = {"data" : (32, 3, 224, 224)}
mx.viz.print_summary(symbol=softmax, shape=shape)
