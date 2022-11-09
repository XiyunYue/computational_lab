import numpy as np 

def MSERESULT(y, y_hat):
    result = np.mean(np.square(y - y_hat))
    return result
