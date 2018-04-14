#-*-coding:utf-8-*-
import os
import sys
import numpy as np
import mxnet as mx
import config

# 保证输出的字符可立即显示
def my_print(str, *args):
    sys.stdout.write(str % args)
    sys.stdout.flush()
    
# 定义网络架构的辅助类
class MyNetwork:
    
    def conv(self, data=None, name=None, n_filter=None, kernel=None):
        return (mx.sym.Convolution(data=data, name=name, kernel=(kernel, kernel), pad=((kernel-1)//2, (kernel-1)//2), num_filter = n_filter, cudnn_tune = config.auto_tune))
    
    def n(self, name=None):
        return self.name + name + str(self.layer)
    
    def act(self, data, name):
        return mx.sym.Activation(data=data, name=self.n(name), act_type="relu")
        
    def bn(self, data, name):
        return mx.sym.BatchNorm(data=data, name=self.n(name), fix_gamma=False)
    
	# 一些常用的单元
    def block(self, data=None, block_type=None, n_filter=None, kernel=None):
        if block_type == 'C':
            conv = self.conv(data=data, name=self.n("conv"), n_filter=n_filter, kernel=kernel)
            return conv
        elif block_type == 'BA':
            bn = self.bn(data, "bn")
            act = self.act(bn, "act")
            return act
        elif block_type == 'CA':
            conv = self.conv(data=data, name=self.n("conv"), n_filter=n_filter, kernel=kernel)
            act = self.act(conv, "act")
            return act
        elif block_type == 'BAC':
            bn = self.bn(data, "bn")
            act = self.act(bn, "act")
            conv = self.conv(data=act, name=self.n("conv"), n_filter=n_filter, kernel=kernel)
            return conv
        elif block_type == 'R-BACBAC': # pre-act残差架构
            identity = data
            bn = self.bn(data, "bnA")
            act = self.act(bn, "actA")
            conv = self.conv(data=act, name=self.n("convA"), n_filter=n_filter, kernel=kernel)
            bn2 = self.bn(conv, "bnB")
            act2 = self.act(bn2, "actB")
            conv2 = self.conv(data=act2, name=self.n("convB"), n_filter=n_filter, kernel=kernel)
            return conv2 + identity
       
	# 可用于定义一串单元
    def MyBlocks(self, data=None, blocks=None, block_type=None, name=None, n_filter=None, kernel=None):

        out = data
        
        for i in range(1, blocks+1):
            self.name = str(name)
            self.layer = i
            out = self.block(out, block_type, n_filter, kernel)
        return out
    