from scipy.io.wavfile import read, write
from scipy.misc import imread, imsave
import matplotlib.pyplot as plt
import numpy as np
import sys

sound_lib_path = '/Users/tru/Desktop/english/'


class Sound():
    def __init__(self, path):
        rate, data = read(path)
        self.rate = rate
        self.data = Sound.flatten(data)

    def write(self, path):
        write(path, self.rate, self.data)

    def get_spectrum(lapse=100, skip=10):
        lapse, channels, skip = opts

        for ts, t in enumerate(range(0, len(sound) - lapse, skip)):
            fft_at_t = np.fft.fft(sound[t:t + lapse])

    @staticmethod
    def flatten(sound):
        if len(sound.shape) > 1:
            sound = sound[:, 0]

        return sound


sounds = [Sound(sound_lib_path + sound) for sound in sys.argv[1:]]
print(sounds)
