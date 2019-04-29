# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import operator


##给出训练集以及对应的类别
def createDataset():
    group=np.array([[1.0,2.0],[1.2,0.1],[0.1,1.4],[0.3,3.5]])
    labels=['A','A','B','B']
    return group,labels
##通过KNN进行分类
def classify(inputs,dataset,label,k):
    dataSize=dataset.shape[0]
    ##计算欧式距离（n维空间两点之间的直线距离）
    diff=np.tile(inputs,(dataSize,1))-dataset
    sqdiff=np.square(diff)
    squareDist=np.sum(sqdiff,axis=1)
    dist=np.sqrt(squareDist)
    
    ##对距离进行排序
    sortedDistIndex=np.argsort(dist)##根据元素的值从大到小对元素进行排序，返回下标
    
    classCount={}
    for i in range(k):
        voteLabel=label[sortedDistIndex[i]]
        ##对选取的k个样本所属的类别个数进行统计
        classCount[voteLabel]=classCount.get(voteLabel,0)+1
        ##选取出现的类别次数最多的类别
        maxCount=0
    for key,value in classCount.items():
        if value>maxCount:
            maxCount=value
            classes=key
    return classes

if __name__=="__main__":
    dataSet,labels=createDataset()
    ##测试数据
    inputs=np.array([1.1,0.3])
    ##最近邻的个数
    K=3  
    output=classify(inputs,dataSet,labels,K)

    print("分类结果",output)