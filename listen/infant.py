from scipy.io.wavfile import read, write
from scipy.misc import imread, imsave
import matplotlib.pyplot as plt
import numpy as np
import math
sounds = '/Users/tru/Desktop/english/'
sample_rate, data = read(sounds + 'tru1.wav')
# 28000 - 50000 -- Hello for calc.wav
data = data[:, 0]

l = 2 ** 14
ch = 2 ** 5
skip = 100
out = np.zeros((len(data) // skip, l // ch))

for ts, t in enumerate(range(0, len(data) - l, skip)):
    ffti = np.fft.fft(data[t:t + l], n=l // ch)
    out[ts] = np.absolute(ffti)

imsave('/Users/tru/Desktop/four.jpeg', out)
