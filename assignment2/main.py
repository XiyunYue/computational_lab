from scipy.io import wavfile
import numpy as np
import time
from tqdm import tqdm
from median import median
from min_w import wmin
from MSE import mse
from scipy import ndimage, misc
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
fs, data = wavfile.read(
    'C:/Users/xliu2/Downloads/PortableGit/newfile/computational_lab/assignment2/data_degraded.wav')
fs, b_k = wavfile.read(
    'C:/Users/xliu2/Downloads/PortableGit/newfile/computational_lab/assignment2/detectionfile.wav')
fs, data_clean = wavfile.read(
    'C:/Users/xliu2/Downloads/PortableGit/newfile/computational_lab/assignment2/clean.wav')
b_k = b_k.reshape(-1, 1)
data = data.reshape(-1, 1)
data_clean = data_clean.reshape(-1, 1)
w_min = wmin(b_k)
print("w need to more than", w_min)
w = 11
data = data.T
b_k = b_k.T
print("data shape = ", data.shape, type(data))
print("b_k shape = ", b_k.shape, type(b_k))
if w % 2 == 0:
    print("w is not an odd number!")
else:
    x = int((w - 1) / 2)
    b_k = b_k.reshape(-1, 1)
    data = data.reshape(-1, 1)
    miss_loca = np.where(b_k != 0)[0]
    miss_loca = miss_loca.reshape(-1, 1)
    data_new = data
    for i in tqdm(range(len(miss_loca))):
        data_filter = data[miss_loca[i][0] - x: miss_loca[i][0] + x + 1]
        output = median(data_filter, w)
        data_new[miss_loca[i][0] - x: miss_loca[i][0] + x + 1] = output
    write("output.wav", fs, data_new)
MSE = mse(data_clean, data_new)
print(MSE)
fig = plt.figure()
plt.plot(data_new)
plt.show()
