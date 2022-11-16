import numpy as np


def median(data, w):
    # print(type(data))
    n = int((w - 1) / 2)
    outputs = np.array(data)
    if w % 2 == 0:
        print("w is not an odd number!")
    else:
        zero_add = [0] * n
        # print(type(zero_add))
        data = zero_add + data + zero_add
        data = np.array(data)
        n_data = len(data) - w + 1
        for i in range(n_data):
            data_filter = data[i: i + 2 * n + 1]
            data_new = np.sort(data_filter)
            outputs[i] = data_new[n]
    return (outputs)
