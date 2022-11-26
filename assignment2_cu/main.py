from scipy.io import wavfile
import numpy as np
import time
from tqdm import tqdm
from MSE import mse
from scipy import ndimage, misc
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from scipy.interpolate import CubicSpline

fs, data = wavfile.read('data_degraded.wav')
fs, b_k = wavfile.read('detectionfile.wav')
fs, data_clean = wavfile.read('clean.wav')
b_k = b_k.reshape(-1, 1)
data = data.reshape(-1, 1)
data_clean = data_clean.reshape(-1, 1)
print("data shape = ", data.shape, type(data))
miss_loca = np.where(b_k != 0)[0]
print("miss_loca = ", miss_loca.shape, type(miss_loca))
miss_loca = miss_loca.reshape(-1, 1)
data_new = data
y = np.delete(data, miss_loca)
x = np.array(range(1, len(data) + 1))
x = np.delete(x, miss_loca)
f = CubicSpline(x, y)

for i in tqdm(range(len(miss_loca))):
    data_new[miss_loca[i]] = f(miss_loca[i])
write("output_cu.wav", fs, data_new)
fig = plt.figure(2)
plt.plot(data_new)
plt.show()
MSE = mse(data_new, data_clean)
print(MSE)
print("Done")
