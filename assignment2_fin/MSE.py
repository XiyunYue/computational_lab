import numpy as np


def mse(data_clean, data_new):
    sum_diff = np.float32(0)
    for i in range(len(data_clean)):
        diff = np.float32(data_clean[i][0] - data_new[i][0])**2
        sum_diff = sum_diff + diff
    accuracy = sum_diff/len(data_clean)
    return accuracy
