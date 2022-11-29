from scipy.io import wavfile
import numpy as np
import time
from tqdm import tqdm
from median_new import median
from MSE import mse
from scipy import ndimage, misc
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import unittest

fs, data = wavfile.read('data_degraded.wav')
fs, b_k = wavfile.read('detectionfile.wav')
fs, data_clean = wavfile.read('clean.wav')
# data shape =  (441001,) <class 'numpy.ndarray'>
# b_k shape =  (441001,) <class 'numpy.ndarray'>
b_k = b_k.reshape(-1, 1)
data = data.reshape(-1, 1)
# data shape =  (441001, 1) <class 'numpy.ndarray'>
# b_k shape =  (441001, 1) <class 'numpy.ndarray'>
data_clean = data_clean.reshape(-1, 1)
miss_loca = np.where(b_k != 0)[0]
miss_loca = miss_loca.reshape(-1, 1)
fig = plt.figure()
plt.plot(data_clean)
plt.show()
print("Done")

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
#print(len(click_cons),len(w))
# w_fft = w[0]
# x = int((w_fft - 1) / 2)
# s = range(miss_loca_new[0] - x, miss_loca_new[0] + click_cons[0] + x)
# data_filter = data[s]
# print(data_filter)
# data_new[s] = median(data_filter, w_fft)
# print(data_new[s])

for i in tqdm(range(len(miss_loca_new))):
    w_fft = w[i]
    x = int((w_fft - 1) / 2)
    s = range(miss_loca_new[i] - x, miss_loca_new[i] + click_cons[i] + x)
    data_filter = data[s]
    data_new[s] = median(data_filter, w_fft)
write("output_me_new.wav", fs, data_new)
MSE = mse(data_clean, data_new)
print(MSE)
# fig = plt.figure()
# plt.plot(data_new)
# plt.show()
# print("Done")



class TestMyCode(unittest.TestCase):
    def test_main_me(self):
        #result = a
        #result_ground = b
        c = [3,4]
        d = [3,4]
        check = np.array_equal(c, d)


if __name__ == '_main_':
    unittest.main()
