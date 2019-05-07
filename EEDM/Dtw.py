# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:57:36 2019

@author: Administrator
"""

import numpy as np
import copy
#在这里用到的是曼哈顿距离（求绝对值距离）
from sklearn.metrics.pairwise import manhattan_distances

s1=[1,2,3,4,5,5,5,4]
s2=[3,4,5,5,5,4]

r,c=len(s1),len(s2)
D0=np.ones((r,c))

D0[0,0]=abs(s1[0]-s2[0])
for i in range(1,r):
    D0[i,0]=abs(s1[i]-s2[0])+D0[i-1,0]
for j in range(1,c):
    D0[0,j]=abs(s1[0]-s2[j])+D0[0,j-1]
for i in range(1,r):
    for j in range(1,c):
        choice=min(D0[i-1,j],D0[i,j-1],D0[i-1,j-1])
        D0[i,j]=choice+abs(s1[i]-s2[j])
print(D0)
