import numpy as np
import time
from tqdm import tqdm
from median import median
from scipy import ndimage, misc


def np_median(data, b_k):
    b_k = b_k.reshape(-1, 1)
    data = data.reshape(-1, 1)
    miss_loca = np.where(b_k != 0)[0]
    miss_loca = miss_loca.reshape(-1, 1)
    data_new = data
    noise_num = 1
    w = []
    miss_loca_new = []
    click_cons = []
    for i in miss_loca:
        if b_k[i + 1] == 0:
            w_new = noise_num * 2 + 1
            w = w + [w_new]
            click_cons = click_cons + [noise_num]
            loca = list(i - noise_num + 1)
            miss_loca_new = miss_loca_new + loca
            noise_num = 1
        else:
            noise_num += 1    
    for i in tqdm(range(len(miss_loca_new))):
        w_fft = w[i]
        x = int((w_fft - 1) / 2)
        s = range(miss_loca_new[i] - x, miss_loca_new[i] + click_cons[i] + x)
        data_filter = data[s]
        #data_new[s] = np.median(data_filter, w_fft)
        data_new[s] = ndimage.median_filter(data_filter, size=w_fft)

    return data_new