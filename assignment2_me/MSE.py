import numpy as np


def mse(data_clean, data_new):
    #accuracy = np.average(np.square(data_clean - data_new), axis=0)


    sum_diff = np.float32(0)
    for i in range(len(data_clean)):
        diff = np.float32((data_clean[i][0] - data_new[i][0])**2)
        sum_diff = sum_diff + diff
    #accuracy_squar = np.sum(np.square(data_clean - data_new))
    #accuracy_squar = np.sum(np.float32(data_clean - data_new)**2)
    accuracy = sum_diff/len(data_clean)
    #accuracy = np.average(accuracy_squar, axis=0)
    return accuracy
