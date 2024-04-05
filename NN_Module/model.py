
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tensorflow import keras
from tensorflow.keras import layers

def make_model(inshape):
   inputs = keras.Input(shape=inshape+(3,))
   x = layers.Rescaling(1.0 / 255.0)(inputs)
   x = layers.Conv2D(32, 5, strides=2, padding="same")(x)
   x = layers.Activation("relu")(x)
   x = layers.Conv2D(48, 5, strides=2, padding="same")(x)
   x = layers.Activation("relu")(x)
   x = layers.Conv2D(64, 5, strides=2, padding="same")(x)
   x = layers.Activation("relu")(x)
   x = layers.Conv2D(64, 5, strides=2, padding="same")(x)
   x = layers.Activation("relu")(x)
   x = layers.Conv2D(76, 3, strides=1, padding="same")(x)
   x = layers.Activation("relu")(x)
   x = layers.Conv2D(76, 3, strides=1, padding="same")(x)
   x = layers.Activation("relu")(x)  
   x = layers.Conv2D(76, 3, strides=1, padding="same")(x)
   x = layers.Activation("relu")(x)  
   x = layers.Dropout(0.5)(x)
   x = layers.Flatten()(x)
   x= layers.Dense(100,activation="relu")(x)
   x= layers.Dense(50,activation="relu")(x)
   x= layers.Dense(20,activation="relu")(x)
   x= layers.Dense(10,activation="relu")(x) 
   outputs= layers.Dense(1)(x)     
   
   return keras.Model(inputs,outputs)        

      
