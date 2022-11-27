import numpy as np


def median(data, w):
    x = int((w - 1) / 2)
    outputs = data
    for i in range(x, len(data) - x):
        data_filter = data[i - x: i + x + 1]
        data_filter = data_filter.T
        data_new = np.sort(data_filter)
        outputs[i][0] = data_new[0][x]
    return (outputs)
