import numpy as np
def mse(data_clean, data_new):
    accuracy = np.average(np.square(data_clean - data_new), axis=0)
    return accuracy