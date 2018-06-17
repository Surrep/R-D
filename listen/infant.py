from scipy.io.wavfile import read, write
from scipy.misc import imread, imsave
import matplotlib.pyplot as plt
import numpy as np
import sys

sound_lib_path = '/Users/tru/Desktop/english/'


def compute_mean_step(old_mean, new_sample, step):
    return old_mean + (1 / step) * (new_sample - old_mean)


def spectrogram(sound, opts=(2 ** 14, 2 ** 5, 5)):
    lapse, channels, skip = opts
    out = np.zeros((len(sound) // skip, lapse // channels))
    brain = np.random.rand(lapse // channels) * 0.01
    brain_file = open('/Users/tru/Desktop/drain.txt', 'w')

    for ts, t in enumerate(range(0, len(sound) - lapse, skip)):
        fft_at_t = np.fft.fft(sound[t:t + lapse], n=lapse // channels)
        out[ts] = np.absolute(fft_at_t)
        print(brain.dot(out[ts]), file=brain_file)

    return out


def flatten(sound):
    if len(sound.shape) > 1:
        sound = sound[:, 0]

    return sound


sounds = [read(sound_lib_path + sound) for sound in sys.argv[1:]]
spectra = [spectrogram(flatten(data[:450000])) for rate, data in sounds]

for i, spectrum in enumerate(spectra):
    imsave('/Users/tru/Desktop/spec{}.jpeg'.format(i), spectrum)
