#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing.image import load_img


class dataset(keras.utils.Sequence) :
    
    def __init__(self,csvfile,batchsize=32,count=None,imgsize=None):
       
      self.batchsize=batchsize
      self.csvfile=csvfile
      self.data=pd.read_csv(self.csvfile)
      
      if count==None:
          self.count=self.data.shape[0]
      else:
          self.count=count
      
      if imgsize==None:
        size=load_img(self.data.iloc[0,0]).size
        self.img_size= (size[1],size[0])
      else:
          self.img_size=imgsize
    
    
    def __len__(self,):
      return  (self.count // self.batchsize)
   
   
    def get_img_shape(self):
       return self.img_size
   
    
    def __getitem__(self,idx):
      i=idx*self.batchsize
      batch_data=self.data.iloc[i:i+self.batchsize]
      x=np.zeros((self.batchsize,)+(self.img_size)+(3,),dtype='uint8') 
      y=np.zeros((self.batchsize,)+(1,))
      for i in range(self.batchsize):    
        imgc=load_img(batch_data.iloc[i,0],target_size=self.img_size)
        imgl=load_img(batch_data.iloc[i,1],target_size=self.img_size)
        imgr=load_img(batch_data.iloc[i,2],target_size=self.img_size)
        x[i]=np.hstack((imgl,imgc,imgr))
        x[i]=imgc                           
        y[i]=(batch_data.iloc[i,3])         
      return x,y


      
