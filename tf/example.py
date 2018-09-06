#coding:utf-8
import tensorflow as tf
import numpy as np

#create data
x_data = np.random.random(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

### create tensorflow structure start ###

