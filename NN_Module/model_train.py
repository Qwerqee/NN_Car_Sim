
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas as pd
from tensorflow import keras
from utils import dataset
from model import make_model
import argparse

parser = argparse.ArgumentParser(description = 'Train the model for self driving car')
parser.add_argument('--train_csv_file',metavar='string',type=str,required = True,help='Path to train driving log csv file')
parser.add_argument('--test_csv_file',metavar='string',type=str,required = True,help='Path to test driving log csv file')
parser.add_argument('--batch_size',metavar='int',type=int,default=32,help='batchsize for training, default: 32')
parser.add_argument('--epochs',metavar='int',type=int,default=10,help='epochs for training, default: 50')

args = parser.parse_args()

batchsize= args.batch_size
epochs = args.epochs

train_csv_file_path=args.train_csv_file
test_csv_file_path=args.test_csv_file

train_ds=dataset(train_csv_file_path,batchsize)
if test_csv_file_path is not None:
   test_ds=dataset(test_csv_file_path,batchsize)
else:
    test_ds=None 

img_shape= train_ds.get_img_shape()  

model=make_model(inshape=img_shape)
model.summary()

loss="mean_squared_error"        
#lrs=[0.001,0.0001,0.00001,0.01]                ----------------------------
lrs=[0.0001] 
#lrs=[0.01, 0.001, 0.0001]

for lr in lrs:
        print("learning rate: "+str(lr))
        print("loss : "+loss)
        callbacks = [
            keras.callbacks.ModelCheckpoint(os.path.join('models',str(lr),str(loss),'save_at_{epoch}.h5'),save_best_only= True),
            keras.callbacks.EarlyStopping(monitor='loss',patience=5,mode='min'),
        ]
        model.compile(
            optimizer=keras.optimizers.Adam(lr),
            loss=loss,
            metrics=loss,
        )
                
        result=model.fit(
            train_ds, validation_data=test_ds, epochs=epochs, callbacks=callbacks,
        )
        
        

      
