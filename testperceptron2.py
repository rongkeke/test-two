#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from __future__ import division
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas
import sklearn.decomposition
def sign(v):
    if v>=0:
        return 1
    else:
        return -1
def train(train_num,train_datas,lr):
    w=0.0
    b=0
    datas_len = len(train_datas)
    alpha = [0 for i in range(datas_len)]
    print 'alpha: ', alpha
    train_array = np.array(train_datas)
    # print "before train_array", train_datas
    print "after train_array\n", train_array
    # print "after train_array1", train_array[1]
    #gram = np.matmul(train_array[:,0:-1] , train_array[:,0:-1].T)
    gram = np.dot(train_array[:,0:2],train_array[:,0:2].T)
    print 'gram:\n',gram
    #print "testcolumn: \n", train_array[:,0:2]
    for for_num in range(train_num):
        row = random.randint(0,datas_len-1)
        yi = train_array[row,-1]
        allsum = 0
        for j in range(datas_len):
            allsum += alpha[j]*train_array[j,-1]*gram[j, row]
        if(yi*allsum<=0):
            alpha[row] += lr
            b += lr*yi
    for i in range(datas_len):
        w += alpha[i]*train_array[i,-1]*train_array[i,0:2]
    print "w", w
    print "b", b
    print "alpha",alpha

    return w,b,alpha,gram

def plot_points(train_datas,w,b):
    plt.figure()
    x1 = np.linspace(0, 8, 100)
    x2 = (-b-w[0]*x1)/(w[1]+1e-10)
    plt.plot(x1, x2, color='r', label='y1 data')
    datas_len=len(train_datas)
    for i in range(datas_len):
        if(train_datas[i][-1]==1):
            plt.scatter(train_datas[i][0],train_datas[i][1],s=50)
        else:
            plt.scatter(train_datas[i][0],train_datas[i][1],marker='x',s=50)
    plt.show()

if __name__=='__main__':
    train_data1 = [[1, 3, 1], [2, 2, 1], [3, 8, 1], [2, 6, 1]]  # 正样本
    train_data2 = [[2, 1, -1], [4, 1, -1], [6, 2, -1], [7, 3, -1]]  # 负样本
    train_datas = train_data1 + train_data2  # 样本集
    w,b,alpha,gram=train(train_num=500,train_datas=train_datas,lr=0.01)
    plot_points(train_datas,w,b)