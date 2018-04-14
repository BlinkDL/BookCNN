#-*-coding:utf-8-*-
import mxnet as mx
import numpy as np
np.core.arrayprint._line_width = 120 # numpy输出行宽

N = 19 # 棋盘大小
features = 8 # 特征层数

first_run = True # 初次运行需要绑定和设置模组

# 载入模型，这里的39540是需装载的epoch
sym, arg_params, aux_params = mx.model.load_checkpoint("model//model", 39540) 
module = mx.mod.Module(symbol=sym, context=[mx.gpu()])

# 输入的数据
data = [[[ 0 for x in range(N) ] for y in range(N)] for c in range(features)]

for x in range(0,N):
    for y in range(0,N):
        data[5][y][x] = 1 # 设置空点的特征层为全1
		
data=np.array([data]) # 变为1*8*19*19，即批大小为1
iter = mx.io.NDArrayIter(data=data) # 设置迭代器

if first_run: # 绑定和设置模组
    module.bind(data_shapes=iter.provide_data)
    module.set_params(arg_params, aux_params)
    first_run = False

pred = module.predict(iter).asnumpy() # 执行网络

# 输出结果
np.set_printoptions(formatter={'all':lambda x: str("%s" % str(int(round(x*100.0,0))).rjust(3))})
print(pred.reshape(N,N))
