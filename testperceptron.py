#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from __future__ import division
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *


def sign(v):
    if v >= 0:
        return 1
    else:
        return -1

def train(train_num, train_datas, lr):  #lr is step's length, train_NUM equal 50
    w=[0,0]
    b=0 # 初始化w.b
    for i in range(train_num):# recursion 50
        print "i", i
        x=random.choice(train_datas)
        x1, x2, y=x
        print "x = ", x
        if(y*sign((w[0]*x1+w[1]*x2+b))<=0):
            w[0]+=lr*y*x1
            w[1]+=lr*y*x2
            b+=lr*y
    print " equation: ", w, b
    return w,b
def plot_points(train_datas, w, b):
    plt.figure()
    x1 = np.linspace(0, 8, 100)
    print "x1 :", x1
    x2 = (-b-w[0]*x1)/w[1]
    plt.plot(x1, x2, color='r', label='y1 data', linestyle = '--',linewidth=2.0)
    plt.xlabel('X')
    plt.ylabel('Y')
    datas_len=len(train_datas)
    for i in range(datas_len):
        if(train_datas[i][-1]==1):
            plt.scatter(train_datas[i][0],train_datas[i][1],s=150)
        else:
            plt.scatter(train_datas[i][0],train_datas[i][1],marker='*',s=150)

    plt.show()


if __name__=='__main__':
    train_data1 = [[1, 3, 1], [2, 2, 1], [3, 8, 1], [2, 6, 1]]  # 正样本
    train_data2 = [[2, 1, -1], [4, 1, -1], [6, 2, -1], [7, 3, -1]]  # 负样本
    train_datas = train_data1 + train_data2  # 样本集
    print "train_datas: ", train_datas
    w, b = train(train_num=50,train_datas=train_datas,lr=0.01)  # lr is step's length
    plot_points(train_datas, w, b)
