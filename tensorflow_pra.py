from __future__ import absolute_import, division, print_function

import tensorflow as tf
tf.enable_eager_execution()

import numpy as np
import os
import time

path_to_file = tf.keras.utils.get_file('shakespeare.txt', 
                                       'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')

with open(path_to_file,"r") as f:
    text = f.read()
    
    
vocab = sorted(set(text))
print ('{} unique characters'.format(len(vocab)))

char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

text_as_int = np.array([char2idx[c] for c in text])

#print('{')
#for char,_ in zip(char2idx, range(20)):
#    print('  {:4s}: {:3d},'.format(repr(char), char2idx[char]))
#print('  ...\n}')
#    
#print ('{} ---- characters mapped to int ---- > {}'.format(repr(text[:13]), text_as_int[:13]))

seq_length = 100
examples_per_epoch = len(text)

char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

for i in char_dataset.take(5):
  print(idx2char[i.numpy()])

print(char_dataset)