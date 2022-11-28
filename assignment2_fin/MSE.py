#Copyright 2022 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
#This file is the function for Calculating mse
#==================================================
"Calculate the mse of repaired audio and clean audio"

import numpy as np


def mse(data_clean, data_new):
    '''
    input the clean data and restorated data

    Args:
        data_clean, data_new:Each of them are numpy.ndarray

    Returns:
        accuracy: a natural number  
    '''
    sum_diff = np.float32(0)

    
    for i in range(len(data_clean)):
        diff = np.float32(data_clean[i][0] - data_new[i][0])**2
        sum_diff = sum_diff + diff
    accuracy = sum_diff/len(data_clean)
    return accuracy
