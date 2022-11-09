import numpy as np
from mseresult import MSERESULT
from Sum import sumOdd
a = np.array([1,2,3,4,5,6])
b = np.array([1,2,3,0,5,6])


mse =  MSERESULT(a,b)
print(mse)

sum = sumOdd(9)
print(sum)