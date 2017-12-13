#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import numpy as np
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print  '我们的数组是：'
print x
print  '\n'
# 切片
z = x[1:4,1:3]
print  '切片之后，我们的数组变为：'
print z
print  '\n'
# 对列使用高级索引
y = x[1:4,[1,2]]
print  '对列使用高级索引来切片：'
print y
meanVal = mean(datMat[nonzero(~isnan(datMat[:, i].A))[0], i])