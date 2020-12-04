# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qa39PDFSPcCXDqd7f0EnGUNdWwLpZjLq
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install mmh3

# Commented out IPython magic to ensure Python compatibility.
# %pip install bitarray

import math
import mmh3
from bitarray import bitarray


class DeletableBloomFilter():

  def __init__(self,n,m,r,k):

    self.n = n
    self.m = m
    self.r = r
    self.k = k

    self.bit_array = bitarray(self.m + self.r)
    self.bit_array.setall(0)

  def add(self, item):

    for i in range(self.k):
      digest = mmh3.hash(item, i) % (self.m)
      if self.bit_array[digest] == True:
        r_bit = self.m - 1 + math.ceil((digest+1) / (math.ceil(self.m/self.r)))
        self.bit_array[r_bit] = True
      else :
        self.bit_array[digest] = True

  def check(self, item):

    for i in range(self.k):
      digest = mmh3.hash(item, i) % (self.m)
      if self.bit_array[digest] == False:
        return False

    return True

  def delete(self,item):
    for i in range(self.k):
      digest = mmh3.hash(item, i) % (self.m)
      r_bit = self.m - 1 + math.ceil((digest+1) / (math.ceil(self.m/self.r)))
      if self.bit_array[digest] == True and self.bit_array[r_bit] == False:
        self.bit_array[digest] = False

k = 3
m = 28
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for item in alpha:
  digests = list()
  for i in range(k):
    digest = mmh3.hash(item, i) % m
    digests.append(digest)
  print('{}:{}'.format(item,digests))

filter = DeletableBloomFilter(4,28,4,3)

filter.add('x')
print(filter.bit_array)
filter.add('y')
print(filter.bit_array)
filter.add('z')
print(filter.bit_array)
filter.add('i')
print(filter.bit_array)

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for a in alpha:
  print(a,filter.check(a))

print(filter.check('x'))
filter.delete('x')
print(filter.bit_array)
print(filter.check('x'))
filter.add('x')
print(filter.bit_array)
print(filter.check('x'))