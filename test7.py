#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import numpy as np
'''
a=np.array([[1,2],[3,4]]) # 1 *4 2* 3
b=np.array([[4,3],[2,1]])
print a*b

x = [1,2,3,4]
print np.cov(x)*3
X=np.array([[1 ,5 ,6] ,[4 ,3 ,9 ],[ 4 ,2 ,9],[ 4 ,7 ,2]])
print np.cov(X)
'''
X=np.array([[1 ,5 ,6] ,[4 ,3 ,9 ],[ 4 ,2 ,9],[ 4 ,7 ,2]])
x=X[0:2]
y=X[2:4]
print "cov(X)", (np.cov(X))
print "cov(X,y)", (np.cov(x,y))
print (2*1.5*1.5+2*0.5*0.5)/3
mean_value = np.mean(X, axis=0)
print mean_value
Xreduce = X - mean_value
print "Xreduce", Xreduce
covMat = np.cov(Xreduce,rowvar=0)
print "covMat", covMat