from scipy.io.wavfile import read, write
from scipy.misc import imread, imsave
import matplotlib.pyplot as plt
import numpy as np
import sys

sound_lib_path = '/Users/tru/Desktop/english/'


class Word():
    def __init__(self, start=0):
        self.start = start
        self.mean = 0
        self.end = 0
        self.step = 1

    def set_end(self, end):
        self.end = end

    def is_anomalous_sample(self, sample, delta=0.8):
        allowed_range = self.mean * delta
        return sample < self.mean - allowed_range or sample > self.mean + allowed_range

    def compute_mean(self, new_sample):
        self.mean = self.mean + (1 / self.step) * (new_sample - self.mean)
        self.step += 1


class Sound():
    def __init__(self, path):
        rate, data = read(path)
        self.rate = rate
        self.data = data

    def write(self, path):
        write(path, self.rate, self.data)

    @classmethod
    def flatten(sound):
        if len(sound.shape) > 1:
        sound = sound[:, 0]

        return sound


def listen(sound, lapse=100, skip):
    lapse, channels, skip = opts

    for ts, t in enumerate(range(0, len(sound) - lapse, skip)):
        fft_at_t = np.fft.fft(sound[t:t + lapse])


sounds = [read(sound_lib_path + sound) for sound in sys.argv[1:]]
flat_sounds = [flatten(data) for rate, data in sounds]
spectra = [spectrogram(flat_sound) for flat_sound in flat_sounds]

spectrum, words = spectra[0]

for i, word in enumerate(words):
    print(i, word.start, word.end)

for i, word in enumerate(words):
    write('/Users/tru/Desktop/nugs/word{}.wav'.format(i),
          44100, flat_sounds[0][word.start:word.end])

# for i, spectrum in enumerate(spectra):
#     imsave('/Users/tru/Desktop/spec{}.jpeg'.format(i), spectrum)
