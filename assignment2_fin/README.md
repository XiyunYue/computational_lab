# Different interpolation methods for audio restoration

## High-level Description of the project

This assignment builds on Assignment I. We assume that we have successfully detected the clicks and we are applying different interpolation methods to restore the audio, such as 
- median filtering
- cubic splines

---

## Installation and Execution                              
matplotlib==3.6.2

numpy==1.23.4

playsound==1.2.2

scipy==1.9.3

tqdm==4.64.1

Afer installing all required packages you can run the demo file simply by typing:

python main_me.py

python main_cu.py


## Methodology and Results
1. Median filtering: 
First we import audio files, detect files and clean files, and convert them into column arrays.
For continuous clicks, the input needs to be selected to ensure that all continuous clicks are filtered out at one time. Therefore, for data processing, use the combination of 'for' and 'if' to find the starting position, duration length and required filter window length of each continuous clicks.
After obtaining these, since we need to display the progress bar of the processing progress, we use the combination of 'for' and 'tqdm' to perform our data processing cycle, filter each clicks, and finally get the result.

2. Cubic Spline: 
For the cubic interpolation method, we also need to import the audio first, and then process the data. In order to use the 'CubicSpline' that comes from python, we need to process the data that can be recognized by the function. Then we need to delete the x, y values corresponding to the noise data in the audio data. Finally, the function can be directly used to obtain the curve, and then the corresponding value can be obtained according to the position of the noise to generate new data.

3. Unit test：
We also performed unit tests on the program. In order to simplify the test, we rewrite the median filter program as a function whose input is audio data and detection data, and the output has only restorated audio data. Because the python system has a median filter function, we can use this compare with our own designed function. Just copy the original function and change the function called in the last part. It will compare the data in two output one by one. Finally, run the unit test, which shows that the output of the two are same.



**Results**

1. For the median filter, different lengths were explored to test the effectiveness of the restoration. We tested the MSE of w from 2*n+1 to 2*n+45 and 2*n+7 was observed to deliver the lowest MSE, as shown in the figure below.
<img src="table.png" width="350">
<img src="MedianFilter_MSEvsLength.png" width="350">

The restored waveform <output_medianFilter.wav> with the optimal filter length is given below:

<img src="wav1.png" width="350">


2. Using the cubic splines, we observe the restored waveform <output_cubicSplines.wav> with the optimal filter length is given below:

<img src="wav2.png" width="350">

3. Comparing the two different interpolation methods, we notice that when the median filter choose the size which has the lowest MSE, the MSE of two methods is not much different, which are 54.62497559898334 (median filter) and 58.03656307490274 (cubic splines).

After listening to the two restored files, we notice the effects of the two methods are similar, which is fix to the difference of their MSE. Both can basically be executed within 1s.

---
**Resources:**
https://en.wikipedia.org/wiki/Markdown
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
Online Readme Editors: https://dillinger.io/ , https://www.makeareadme.com
https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/
Docstrings: https://www.programiz.com/python-programming/docstrings
https://numpy.org/doc/stable/user/quickstart.html
Numpy for matlab users https://numpy.org/doc/stable/user/numpy-for-matlab-users.html
Progress bars: https://pypi.org/project/progress/
Audio Basics in Python: https://www.it-jim.com/blog/audio-processing-basics-in-python/
Unittesting: 
https://docs.python.org/3/library/unittest.html
https://colab.research.google.com/github/damorimRG/practical_testing_book/blob/master/testgranularity/unittesting.ipynb






