#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import numpy as np
from numpy import *
a = np.arange(10)
print a
print a[2:5]
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print a
print "a[..., 2]: ", a[..., 2]
print "a[1,...]: ", a[1, ...]
print "a[:,1].A", a[:, 1].A
print "==============================================="
x = np.array([[1,  2],  [3,  4],  [5,  6]])
y = x[[0,1,2],  [0,1,0]]
print y