from scipy.io import wavfile
import numpy as np
import time
from tqdm import tqdm
from median import median
from MSE import mse
from scipy import ndimage, misc
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
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
data_new = data
for i in tqdm(range(len(miss_loca))):
    noise_num = 1
    if b_k[miss_loca[i] + 1] != 0:
        noise_num += 1 
        i += 1
    w = noise_num * 2 + 1
    print(w)
    x = int((w - 1) / 2)
    data_filter = data[miss_loca[i][0] - x: miss_loca[i][0] + x + 1]
    output = median(data_filter, w)
    data_new[miss_loca[i][0] - x: miss_loca[i][0] + x + 1] = output
write("output_me_new.wav", fs, data_new)
MSE = mse(data_clean, data_new)
print(MSE)
fig = plt.figure()
plt.plot(data_new)
plt.show()
print("Done")