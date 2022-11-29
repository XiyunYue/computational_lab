#Copyright 2022 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
#This file is the main code of median filter, which is assignment2 of computational method.
#==================================================
"use median filter for audio restoration "


from scipy.io import wavfile
import numpy as np
import time
from tqdm import tqdm
from median import median
from MSE import mse
from scipy import ndimage, misc
import matplotlib.pyplot as plt
from playsound import playsound
from scipy.io.wavfile import write
from playsound import playsound



#input the data from assignment1 matlab code
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

#Calculate the filter window size required for clicks at different positions
#merge consecutive clicks into one detection area
data_new = data
noise_num = 1
w = []
miss_loca_new = []
click_cons = []
for i in miss_loca:
    if b_k[i + 1] == 0:
        w_new = noise_num * 2 + 49
        w = w + [w_new]
        click_cons = click_cons + [noise_num]
        loca = list(i - noise_num + 1)
        miss_loca_new = miss_loca_new + loca
        noise_num = 1
    else:
        noise_num += 1


#Use median filter to repair each noise point
start_time = time.time()
for i in tqdm(range(len(miss_loca_new))):
    w_fft = w[i]
    x = int((w_fft - 1) / 2)
    s = range(miss_loca_new[i] - x, miss_loca_new[i] + click_cons[i] + x)
    data_filter = data[s]
    data_new[s] = median(data_filter, w_fft)
end_time = time.time()
execution_time = end_time - start_time
print('The execution time in seconds is :', execution_time)
#make the output audio and play it
write("output_medianFilter.wav", fs, data_new)
playsound("data_degraded.wav")
playsound("output_me.wav")
fig = plt.figure(2)
plt.plot(data_new)
plt.xlabel("No. of Samples")
plt.ylabel("Amplitude")
plt.title("Signal After Median Filtering")
plt.show()



#Calculate MSE
MSE1 = mse(data_clean, data_new)
print(MSE1)
print("Done")
