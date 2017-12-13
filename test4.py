#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import numpy as np
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print  '我们的数组是：'
print x
print  '\n'
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
print 'rows', rows
print 'cols', cols
y = x[rows,cols]
print  '这个数组的每个角处的元素是：'
print y