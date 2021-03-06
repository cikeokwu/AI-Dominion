import random
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense,Convolution2D, Conv2D, Flatten, Permute, Activation
from keras.initializers import VarianceScaling
from keras import backend as K
import tensorflow as tf

INPUT_SHAPE = (84, 84)
WINDOW_LENGTH = 4



def model0(game):
    model = Sequential()
    model.add(Permute((2, 3, 1), input_shape=game.input_shape))
    model.add(Convolution2D(32, (8, 8), strides=(4, 4)))
    model.add(Activation('relu'))
    model.add(Convolution2D(64, (4, 4), strides=(2, 2)))
    model.add(Activation('relu'))
    model.add(Convolution2D(64, (3, 3), strides=(1, 1)))
    model.add(Activation('relu'))
    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dense(game.action_size))
    model.add(Activation('linear'))
    return model

def model1(game):
    model = Sequential()
    # (width, height, channels)
    model.add(Permute((2, 3, 1), input_shape=game.input_shape))
    model.add(Convolution2D(16, (8, 8), strides=(4, 4)))
    model.add(Activation('relu'))
    model.add(Convolution2D(32, (4, 4), strides=(2, 2)))
    model.add(Activation('relu'))
    model.add(Flatten())
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(Dense(game.action_size))
    model.add(Activation('linear'))
    return model

def model2(game):
    intializer = VarianceScaling()
    model = Sequential()
    model.add(Permute((2, 3, 1), input_shape=game.input_shape))
    model.add(Conv2D(filters=32, kernel_size=(8, 8), strides=(4, 4), padding="same", activation="relu",
                     kernel_initializer=intializer))
    model.add(Conv2D(filters=64, kernel_size=(4, 4), strides=(2, 2), padding="same", activation="relu",
                     kernel_initializer=intializer))
    model.add(Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1), padding="same", activation="relu",
                     kernel_initializer=intializer))
    model.add(Flatten())
    model.add(Dense(512, input_shape=(11, 11, 64), activation='relu'))
    model.add(Dense(game.action_size, activation='linear'))
    return model