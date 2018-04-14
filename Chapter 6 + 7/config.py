#-*-coding:utf-8-*-
import numpy as np
import mxnet as mx

np.core.arrayprint._line_width = 120 # numpy输出行宽

data_device = mx.gpu()
train_device = [mx.gpu()]
auto_tune = 'fastest' # 使用最快的卷积算法

model_directory = "model" # 储存模型的目录
model_prefix = model_directory + "//model" # 模型的文件名前缀
n_epoch_load = 0 # 从哪个epoch继续训练

apply_symmetry = True # 是否使用棋盘的8种对称性
shuffle_data = True # 是否打散数据

save_period = 60 # 储存模型+测试模型+调整学习速率的间隔

batch_size = 256 # 批大小
learning_rate = 0.1 # 学习速率
wd = 0 # L2正则化强度
learning_decay = 0.9 # 每次调整学习速率的衰减度
exit_learning_rate = 0.01 # 在学习速率衰减到多少时退出训练

train_prefix = "tygem//TygemAmateur" # 数据的文件名前缀
train_begin_index = 6 # 训练开始于哪个文件
train_end_index = 597 # 训练结束于哪个文件

head = 2 # 数据文件中头部的大小（这里用2个字节储存落子位置）
