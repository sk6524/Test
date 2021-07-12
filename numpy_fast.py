#numpy module execution is faster than lists
import numpy as np
import time
import sys

SIZE = 1000000
l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.array(SIZE)
a2 = np.arange(SIZE)

#python list
start = time.time()
result = [x+y for x,y in zip(l1,l2)]
print("python list look:",(time.time()-start)*1000)

#numpy array
start = time.time()
result = a1+a2
print("numpy look",(time.time()-start)*1000)

#When you are processing millions and millions of secons you just use numpy module