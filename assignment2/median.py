import numpy as np


def median(data, w):
    n = int((w - 1) / 2)
    outputs = data
    data = np.append(data, [0] * n)
    data = np.insert(data, 0, [0] * n)
    for i in range(w):
        data_filter = data[i: i + w + 1]
        data_new = np.sort(data_filter)
        outputs[i] = data_new[n]
    return (outputs)

