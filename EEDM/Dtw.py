# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:57:36 2019

@author: Administrator
"""

import numpy as np

def dtw_distance(ts_a,ts_b,d=lambda x,y:abs(x-y),mww=10000):
    ts_a,ts_b=np.array(ts_a),np.array(ts_b)
    M,N=len(ts_a),len(ts_b)
    cost=np.zeros((M,N))
    
    cost[0,0]=d(ts_a[0],ts_b[0])
    for i in range(1,M):
        cost[i,0]=cost[i-1,0]+d(ts_a[i],ts_b[0])
        
    for j in range(1,N):
        cost[0,j]=cost[0,j-1]+d(ts_a[0],ts_b[j])
    print(cost)
    for i in range(1,M):
        for j in range(1,N):
            choice=min(cost[i-1,j-1],cost[i,j-1],cost[i-1,j])
            cost[i,j]=choice+d(ts_a[i],ts_b[j])
            
    return cost
if __name__=="__main__":
    
    s1=[1,2,3,4,5,5,5,4]
    s2=[3,4,5,5,5,4]
    print(dtw_distance(s1,s2)[-1,-1])