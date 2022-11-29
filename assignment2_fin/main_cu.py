#Copyright 2022 by Xiaoru Liu, Trinity College Dublin. All rights reserved.
#
#This file is the main code of cubic splines, which is assignment2 of computational method.
#==================================================
"use cubic splines for audio restoration "

from scipy.io import wavfile
import numpy as np
import time
from tqdm import tqdm
from MSE import mse
from scipy import ndimage, misc
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from scipy.interpolate import CubicSpline
from playsound import playsound

#input the data from assignment1 matlab code
fs, data = wavfile.read('data_degraded.wav')
fs, b_k = wavfile.read('detectionfile.wav')
fs, data_clean = wavfile.read('clean.wav')

fig = plt.figure(1)
plt.subplots_adjust(hspace = 0.7)
plt.subplot(211)
plt.plot(data)
plt.xlabel("No. of Samples", fontsize=15)
plt.ylabel("Amplitude", fontsize=15)
plt.title("Clean Signal", fontsize=15)

plt.subplot(212)
plt.plot(data_clean)
plt.xlabel("No. of Samples", fontsize=15)
plt.ylabel("Amplitude", fontsize=15)
plt.title("Degraded Signal", fontsize=15)
plt.show()

#make the datas in the same shape
b_k = b_k.reshape(-1, 1)
data = data.reshape(-1, 1)
data_clean = data_clean.reshape(-1, 1)
miss_loca = np.where(b_k != 0)[0]
miss_loca = miss_loca.reshape(-1, 1)

#make the x,y for the CubicSpline
data_new = data
y = np.delete(data, miss_loca)
x = np.array(range(1, len(data) + 1))
x = np.delete(x, miss_loca)
f = CubicSpline(x, y)


#Use the obtained function to repair each noise point
start_time = time.time()
for i in tqdm(range(len(miss_loca))):
    data_new[miss_loca[i]] = f(miss_loca[i])
end_time = time.time()
execution_time = end_time - start_time
print('The execution time in seconds is :', execution_time)

#make the output audio and play it
write("output_cubicSplines.wav", fs, data_new)
#print(type(data_new),data_new.shape)
playsound("data_degraded.wav")
playsound("output_me.wav")

# fig = plt.figure(2)
# plt.plot(data_new)
# plt.xlabel("No. of Samples")
# plt.ylabel("Amplitude")
# plt.title("Signal After Cubic Splines")
# plt.show()

MSE = mse(data_new, data_clean)
print(MSE)
print("Done")


