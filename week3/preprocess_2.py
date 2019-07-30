# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 18:36:52 2019

"""
import numpy as np
import pandas as pd
import datetime as dt

PATH_TO_PROCESSED_DATA = 'D:\\Mala GD projects\\Session based RNN recommendation\\GRU4Rec-master\\GD\\'
#data_tr_full = pd.read_csv(PATH_TO_PROCESSED_DATA + 'rsc15_train_full.txt', sep='\t', usecols=[0,1,2])
data_tr = pd.read_csv(PATH_TO_PROCESSED_DATA + 'sessions_train.csv', sep=',', usecols=[0,3,4])
data_tr.columns = ["SessionId", "ItemId", "Time"]
data_tr.to_csv(PATH_TO_PROCESSED_DATA + 'sessions_train_trimmed.csv', sep=',', index=False)

data_test = pd.read_csv(PATH_TO_PROCESSED_DATA + 'sessions_test.csv', sep=',', usecols=[0,3,4])
data_test.columns = ["SessionId", "ItemId", "Time"]
data_test.to_csv(PATH_TO_PROCESSED_DATA + 'sessions_test_trimmed.csv', sep=',', index=False)
