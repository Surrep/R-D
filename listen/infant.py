from scipy.io.wavfile import read, write
from scipy.misc import imread, imsave
import matplotlib.pyplot as plt
import numpy as np
import sys

sound_lib_path = '/Users/tru/Desktop/english/'
# sample_rate, data = read(sounds + 'tru1.wav')
# 28000 - 50000 -- Hello for calc.wav


def create_time_fourier(sound, opts=(2 ** 14, 2 ** 5, 100)):
    lapse, channels, skip = opts
    out = np.zeros((len(sound) // skip, lapse // channels))

    for ts, t in enumerate(range(0, len(sound) - lapse, skip)):
        fft_at_t = np.fft.fft(sound[t:t + lapse], n=lapse // channels)
        out[ts] = np.absolute(fft_at_t)

    return out


sounds = [read(sound_lib_path + sound) for sound in sys.argv[1:]]
spectra = [create_time_fourier(data) for rate, data in sounds]

# imsave('/Users/tru/Desktop/four.jpeg', out)
