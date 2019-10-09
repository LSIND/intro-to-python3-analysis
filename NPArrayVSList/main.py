#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import numpy as np
import time, sys

SIZE = 10000000

L1 = range(SIZE) # lists L1 = L2 = [0,1,2,...,100000000]
L2 = range(SIZE)

N1 = np.arange(SIZE) # NP Array N1 = N2 = [0,1,2,...,100000000]
N2 = np.arange(SIZE)

start = time.time()
result = [(x,y) for x,y in zip(L1,L2)] # merge two lists
t_list = time.time()-start
print("Time of merging lists:", t_list)

start = time.time()
result = N1 + N2 # merge two numpy arrays
t_npa = time.time()-start
print("Time of merging numpy arrays:", t_npa)

print("Numpy array is {:2.4f} times faster ".format(t_list/t_npa))
