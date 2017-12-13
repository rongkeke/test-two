#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import numpy as np
import time
a = np.random.randn(5, 1)
print a.reshape((5, 1))
print 'ending'

a = np.random.rand(1000000)
b = np.random.rand(1000000)
tic = time.time()
c = np.dot(a, b)
toc = time.time()
print c
print 'Vectorized version:' + str(1000 * (toc-tic)) + 'ms'


c = 0
tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time()
print c
print 'Loop version:' + str(1000 * (toc-tic)) + 'ms'


a1 = np.array([1, 2, 3, 4])
print a

print np.random.rand(10)
print np.array([1, 2, 3, 4])
print np.zeros((3, 1))
A = np.array([[56.0, 0.0, 4.4, 68.0],
              [1.2, 104.0, 52.0, 8.0],
              [1.8, 135.0, 99.0, 0.9]])
print 'A+1 = ', A+1
cal = A.sum(axis=0)
print 'cal = ', cal
print '=============='
print cal.reshape(1, 4)
print '=============='
print 100*A/cal.reshape(1, 4)
