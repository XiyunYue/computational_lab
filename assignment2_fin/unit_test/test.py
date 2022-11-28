import unittest
from scipy.io import wavfile
import numpy as np
import time
from tqdm import tqdm
from median import median
from scipy import ndimage, misc
from my_median import my_median
from np_median import np_median

fs, data = wavfile.read('data_degraded.wav')
fs, b_k = wavfile.read('detectionfile.wav')
a = my_median(data, b_k)
b = np_median(data, b_k)


class TestMyCode(unittest.TestCase):
    def test_main_me(self):
        result = a
        result_ground = b
        check = np.array_equal(result, result_ground)


if __name__ == '__main__':
    unittest.main()
