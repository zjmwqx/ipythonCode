
# coding: utf-8

# In[1]:

import re
import logging
import traceback
import os
import sys
import commands

#read in data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



train_h = pd.read_csv("../corpus/train.data", sep="\t",header=0,names=["id","label","content"], encoding="utf-8").dropna()

ng_df = train_h[train_h.label == 'n']
ng_df.shape
pos_df = train_h[train_h.label == 'y']
pos_df.shape

import jieba
import jieba.posseg as pseg
jieba.enable_parallel(4)
def segmenter(line):
    words = pseg.cut(line)
    return list(words)


seg1 = pd.read_pickle("seg1")
seg2 = pd.read_pickle("seg2")
seg3 = pd.read_pickle("seg3")
seg4_5 = pd.read_pickle("seg4_5")
seg4_10 = pd.read_pickle("seg4_10")
seg = pd.concat([seg1, seg2, seg3, seg4_5, seg4_10])
seg1 = 0
seg2 = 0
seg3 = 0
seg4_5 = 0
seg4_10 = 0
train_h['seg'] = seg
seg = 0
train_h.to_pickle("corpus_train")
