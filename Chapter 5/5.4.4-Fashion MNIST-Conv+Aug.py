#-*-coding:utf-8-*-
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

# 用于辅助定义网络，这是深度卷积网络中常用的"卷积-BN-非线性"模块
def CBA(src, suffix, num_filter, kernel, pad):
    conv = mx.sym.Convolution(data=src, name="conv"+suffix, kernel=(kernel,kernel), pad=(pad,pad), num_filter=num_filter)
    bn = mx.sym.BatchNorm(data=conv, name="bn"+suffix, fix_gamma=False)
    act = mx.sym.Activation(data=bn, name="act"+suffix, act_type="relu")
    return act

# 由于辅助定义网络，这里在每2个卷积层后加1个池化层
def LAYER(src, layer, num_filter, pad):
    conv1 = CBA(src, layer+"1", num_filter, 3, pad)
    conv2 = CBA(conv1, layer+"2", num_filter, 3, pad)
    pool = mx.sym.Pooling(data=conv2, name="pool"+layer, pool_type="max", kernel=(2,2), stride=(2,2))
    return pool

# 设置网络
data = mx.symbol.Variable('data')
# 将3*28*28变换为32*14*14
net = LAYER(data, "1", 32, 1)
# 将32*14*14变换为64*7*7
net = LAYER(net, "2", 64, 1)
# 将64*7*7变换为64*3*3
net = LAYER(net, "3", 64, 1)
# 将64*3*3变换为128*1*1
net = CBA(net, "4", 128, 3, 0)
# 将128*1*1变换为10*1*1
net = mx.sym.Convolution(data=net, name="final", kernel=(1,1), num_filter=10)
# 将10*1*1变换为10
net = mx.sym.Flatten(data=net, name="flatten")
net = mx.sym.SoftmaxOutput(data=net, name='softmax')

# 输出参数情况供参考
shape = {"data" : (batch_size, 1, 28, 28)}
mx.viz.print_summary(symbol=net, shape=shape)

# 由于训练数据多，这里采用了GPU，若读者没有GPU，可修改为CPU
module = mx.mod.Module(symbol=net, context=mx.gpu(0))

# 迭代器：测试数据
val_iter = mx.io.NDArrayIter(val_img, val_lbl, batch_size) 

# 手动循环40个epoch
for epoch in range(40):
    # 生成增强的图像，最佳方法是在另一进程执行，这里只是演示
    # 首先复制一份原始图像
    aug_img = train_img.copy()
    # 修改其中的每幅图像
    for i in range(aug_img.shape[0]):
        # 有50%概率做左右翻转
        if np.random.random() < 0.5:
            # aug_img[i][0]为第i号样本的0号通道，灰度图像只有0号通道
            # fliplr()用于左右翻转
            aug_img[i][0] = np.fliplr(aug_img[i][0])
            
        # 左右移动最多2个像素，注意randint(a,b)的范围为a到b-1
        amt = np.random.randint(0, 3)
        if amt > 0: # 如果需要移动…
            if np.random.random() < 0.5: # 左移动还是右移动？
                # pad()用于加上外衬，因移动后减少的区域需补零
                # 然后用[:]取所要的部分
                aug_img[i][0] = np.pad(aug_img[i][0],((0,0),(amt,0)), mode='constant')[:, :-amt]
            else:
                aug_img[i][0] = np.pad(aug_img[i][0],((0,0),(0,amt)), mode='constant')[:, amt:]
        
        # 上下移动最多2个像素
        amt = np.random.randint(0, 3)
        if amt > 0:
            if np.random.random() < 0.5:
                aug_img[i][0] = np.pad(aug_img[i][0],((amt,0),(0,0)), mode='constant')[:-amt, :]
            else:
                aug_img[i][0] = np.pad(aug_img[i][0],((0,amt),(0,0)), mode='constant')[amt:, :]
        
        # 随机清零最大5*5的区域
        x_size = np.random.randint(1, 6)
        y_size = np.random.randint(1, 6)
        x_begin = np.random.randint(0, 28-x_size+1)
        y_begin = np.random.randint(0, 28-y_size+1)
        aug_img[i][0][x_begin:x_begin+x_size, y_begin:y_begin+y_size] = 0
        
    # 每个epoch重设训练数据
    train_iter = mx.io.NDArrayIter(aug_img, train_lbl, batch_size, shuffle=True)
    # 每个epoch降低学习速率
    lr = 0.06 * pow(0.95, epoch)
    # 输出当前epoch信息
    print("epoch " + str(epoch) + ", learning rate = " + str(lr))
    # 训练
    module.fit(
        train_iter,
        eval_data=val_iter,
        optimizer = 'sgd', 
        optimizer_params = {'learning_rate' : lr},
        num_epoch = 1, # 每次训练1个epoch
        batch_end_callback = mx.callback.Speedometer(batch_size, 60000/batch_size)
    )
