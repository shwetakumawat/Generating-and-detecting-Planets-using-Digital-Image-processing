# recreation of the exoplanet-ml neural network with keras 

import keras 
import numpy as np

from keras.layers import Input, Dense, Conv1D, MaxPooling1D, Concatenate, Flatten
from keras.models import Model

# global view input
input_global = Input(shape=(2001,1))
x = Conv1D(16, 5, strides=1)(input_global)
x = Conv1D(16, 5, strides=1)(x)
x = MaxPooling1D(pool_size=5, strides=2)(x)
x = Conv1D(32, 5, strides=1)(x)
x = Conv1D(32, 5, strides=1)(x)
x = MaxPooling1D(pool_size=5, strides=2)(x)
x = Conv1D(64, 5, strides=1)(x)
x = Conv1D(64, 5, strides=1)(x)
x = MaxPooling1D(pool_size=5, strides=2)(x)
x = Conv1D(128, 5, strides=1)(x)
x = Conv1D(128, 5, strides=1)(x)
x = MaxPooling1D(pool_size=5, strides=2)(x)
x = Conv1D(256, 5, strides=1)(x)
x = Conv1D(256, 5, strides=1)(x)
x = MaxPooling1D(pool_size=5, strides=2)(x)

# local view 
input_local = Input(shape=(201,1))
y = Conv1D(16, 5, strides=1)(input_local)
y = Conv1D(16, 5, strides=1)(y)
y = MaxPooling1D(pool_size=7, strides=2)(y)
y = Conv1D(32, 5, strides=1)(y)
y = Conv1D(32, 5, strides=1)(y)
y = MaxPooling1D(pool_size=7, strides=2)(y)

# merge layers for fully connected
xf = Flatten()(x)
yf = Flatten()(y)
z = Concatenate()([xf,yf])
z = Dense(512, activation='relu')(z)
z = Dense(512, activation='relu')(z)
z = Dense(512, activation='relu')(z)

output = Dense(1, activation='sigmoid', name='main_output')(z)

model = Model(inputs=[input_global, input_local], outputs=output)

'''
model.summary()
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to
==================================================================================================
input_1 (InputLayer)            (None, 2001, 1)      0
__________________________________________________________________________________________________
conv1d_1 (Conv1D)               (None, 1997, 16)     96          input_1[0][0]
__________________________________________________________________________________________________
conv1d_2 (Conv1D)               (None, 1993, 16)     1296        conv1d_1[0][0]
__________________________________________________________________________________________________
max_pooling1d_1 (MaxPooling1D)  (None, 995, 16)      0           conv1d_2[0][0]
__________________________________________________________________________________________________
conv1d_3 (Conv1D)               (None, 991, 32)      2592        max_pooling1d_1[0][0]
__________________________________________________________________________________________________
conv1d_4 (Conv1D)               (None, 987, 32)      5152        conv1d_3[0][0]
__________________________________________________________________________________________________
max_pooling1d_2 (MaxPooling1D)  (None, 492, 32)      0           conv1d_4[0][0]
__________________________________________________________________________________________________
conv1d_5 (Conv1D)               (None, 488, 64)      10304       max_pooling1d_2[0][0]
__________________________________________________________________________________________________
conv1d_6 (Conv1D)               (None, 484, 64)      20544       conv1d_5[0][0]
__________________________________________________________________________________________________
max_pooling1d_3 (MaxPooling1D)  (None, 240, 64)      0           conv1d_6[0][0]
__________________________________________________________________________________________________
input_2 (InputLayer)            (None, 201, 1)       0
__________________________________________________________________________________________________
conv1d_7 (Conv1D)               (None, 236, 128)     41088       max_pooling1d_3[0][0]
__________________________________________________________________________________________________
conv1d_11 (Conv1D)              (None, 197, 16)      96          input_2[0][0]
__________________________________________________________________________________________________
conv1d_8 (Conv1D)               (None, 232, 128)     82048       conv1d_7[0][0]
__________________________________________________________________________________________________
conv1d_12 (Conv1D)              (None, 193, 16)      1296        conv1d_11[0][0]
__________________________________________________________________________________________________
max_pooling1d_4 (MaxPooling1D)  (None, 114, 128)     0           conv1d_8[0][0]
__________________________________________________________________________________________________
max_pooling1d_6 (MaxPooling1D)  (None, 94, 16)       0           conv1d_12[0][0]
__________________________________________________________________________________________________
conv1d_9 (Conv1D)               (None, 110, 256)     164096      max_pooling1d_4[0][0]
__________________________________________________________________________________________________
conv1d_13 (Conv1D)              (None, 90, 32)       2592        max_pooling1d_6[0][0]
__________________________________________________________________________________________________
conv1d_10 (Conv1D)              (None, 106, 256)     327936      conv1d_9[0][0]
__________________________________________________________________________________________________
conv1d_14 (Conv1D)              (None, 86, 32)       5152        conv1d_13[0][0]
__________________________________________________________________________________________________
max_pooling1d_5 (MaxPooling1D)  (None, 51, 256)      0           conv1d_10[0][0]
__________________________________________________________________________________________________
max_pooling1d_7 (MaxPooling1D)  (None, 40, 32)       0           conv1d_14[0][0]
__________________________________________________________________________________________________
flatten_1 (Flatten)             (None, 13056)        0           max_pooling1d_5[0][0]
Trainable params: 8,530,657
Non-trainable params: 0
__________________________________________________________________________________________________

'''