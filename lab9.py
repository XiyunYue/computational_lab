import numpy as np
from median import median
from scipy import ndimage, misc

data = [1, 2, 3, 6, 10, 1, 2, 5, 6, 5, 10, 7, 2, 1]
# print(type(data))
w = 3
data_mew = median(data, w)
print(data_mew)

data_py = ndimage.median_filter(data, size=w, mode='constant')
print(data_py)
