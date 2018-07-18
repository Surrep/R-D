from scipy.io.wavfile import read, write
from scipy.misc import imread, imsave
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import sys

sound_lib_path = '/Users/tru/Desktop/'


class Sound():
    def __init__(self, path):
        rate, data = read(path)
        self.rate = rate
        self.data = Sound.flatten(data)

    def write(self, path):
        write(path, self.rate, self.data)

    def get_frequencies(self, start=None, end=None):
        if start is None or end is None:
            start = 0
            end = len(self.data)

        return np.fft.fft(self.data[start:end])

    @staticmethod
    def flatten(sound):
        if len(sound.shape) > 1:
            sound = sound[:, 0]

        return sound


sounds = [Sound(sound_lib_path + sound) for sound in sys.argv[1:]]
s0 = sounds[0]


fig = plt.figure()
graph, = plt.plot([], [], 'o')


def animate(i):
    freqs = s0.get_frequencies(i, i + 100)
    freqs /= np.max(np.absolute(freqs))
    graph.set_data(freqs.real, freqs.imag)
    return graph


ani = animation.FuncAnimation(
    fig, animate, frames=100, interval=200)

plt.show()
