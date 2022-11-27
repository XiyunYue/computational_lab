# Add here a title for the project
Different interpolation methods for audio restoration


## High-level Description of the project
This assignment builds on Assignment I. We assume that we have successfully detected the clicks and we are applying different interpolation methods to restore the audio, such as
- median filtering
- cubic splines

---

## Installation and Execution                              
pip install numpy
pip install scipy
pip install tqdm
pip install matplotlib
pip install matplotlib


pipreqs $project/path/requirements.txt
```
For more details check [here](https://github.com/bndr/pipreqs)


Afer installing all required packages you can run the demo file simply by typing:
```sh
python main_me.py
python main_cu.py

## Methodology and Results
1. Median filtering: first import audio files, detect files and clean files, and convert them into column arrays.
Since we choose to filter only on clicks, and for continuous clicks, the entire area needs to be selected to ensure that all continuous clicks are filtered out at one time. Therefore, for data processing, use the combination of for and if to find the starting position of each continuous clicks , duration length and required filter window length.
After obtaining these three, since we need to display the progress bar of the processing progress, we use the combination of for and tqdm to perform our data processing cycle, filter each clicks, and finally get the result.

cubicSpline: For the cubic interpolation method, you also need to import the audio first, and then process the data.

In order to use the CubicSpline that comes with python, we need to process the data into an x, y curve that can be recognized by the function, and then delete the x, y values corresponding to the noise data in the audio data. Finally, the function can be directly used to obtain the curve, and then the corresponding value can be obtained according to the position of the noise to generate new data.



**Results**

1. For the median filter, different lengths were explored to test the effectiveness of the restoration. We tested the MSE of w from 2*n+1 to 2*n+45 and 2*n+7 was observed to deliver the lowest MSE, as shown in the figure below.

<img src="MedianFilter_MSEvsLength.png" width="350">

The restored waveform <output_medianFilter.wav> with the optimal filter length is given below:
<img src="wav1.png" width="350">


2. Using the cubic splines, we observe the restored waveform <output_cubicSplines.wav> with the optimal filter length is given below:
<img src="wav2.png" width="350">

3. Comparing the two different interpolation methods, we notice that When the median filter takes the lowest MSE, the MSE of the two methods is not much different, which are 54.62497559898334 (median filter) and 58.03656307490274 (cubic splines).They can all be run in a very short time.

After listening to the two restored files, we notice the filtering effects of the two methods are similar, and there is no big difference in their MSE.


---
## Credits

This code was developed for purely academic purposes by XXXX (add github profile name) as part of the module ..... 

Resources:
- XXXX
- XXX




