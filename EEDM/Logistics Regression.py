# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:55:51 2019

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.preprocessing import LabelEncoder
from scipy.sparse import csr_matrix,hstack
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import log_loss

def loadData():
    datadir='E:/warehouse/talkingdata'
    getrain=pd.read_csv(os.path.join(datadir,'gender_age_train.csv'),index_col='device_id')
    gettest=pd.read_csv(os.path.join(datadir,'gender_age_test.csv'),index_col='device_id')
    phone=pd.read_csv(os.path.join(datadir,'phone_brand_device_model'))
    
   #删除手机设备中重复的id
    phone=phone.drop_duplicates('device_id',keep='first').set_index('device_id')
    events=pd.read_csv(os.path.join(datadir,'events.csv'),parse_dates=['timestamp'],index_col='event_id')
    appevents=pd.read_csv(os.path.join(datadir,'app_events.csv'),usecols=['event_id','app_id','is_active'],dtype={'is_active':bool})
    applabels=pd.read_csv(os.path.join(datadir,'app_label.csv'))
    
    
    #feature engineering特征工程 
    #phone brand
    getrain['trainrow']=np.arange(getrain.shape(0))
    gettest['testrow']=np.arange(gettest.shape(0))
    
    