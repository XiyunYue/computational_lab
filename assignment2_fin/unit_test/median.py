#Copyright 2022 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
#This file is the function for median filter
#==================================================
"Create a median filter "
import numpy as np


def median(data, w):
    '''
    input the data that is going to be filtered and window size

    Args:
        adta: numpy.ndarray
        w: a natural number

    Returns:
        outputs: numpy.ndarray. The shape is the same as the input data 
    '''
    x = int((w - 1) / 2)
    outputs = data
    for i in range(x, len(data) - x):
        data_filter = data[i - x: i + x + 1]
        data_filter = data_filter.T
        data_new = np.sort(data_filter)
        outputs[i][0] = data_new[0][x]
    return (outputs)
