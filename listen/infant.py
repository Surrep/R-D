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


sounds = [Sound(sound_lib_path + file) for file in sys.argv[1:]]
s0 = sounds[0]
print(len(s0.data))


def get_colors(r, g, b):
    return np.mgrid[:255:complex(r), 0:255:complex(g), 0:255:complex(b)].reshape(3, -1).T


offset = 30000
freq_bins = 200
colors = (1, 2, 6)
num_plots = np.prod(colors)


color_seq = get_colors(*colors)
fig, axes = plt.subplots(num_plots, 1)
graphs = [None] * num_plots
freq_ranges = np.linspace(0, freq_bins / 2, num_plots + 1).astype(np.int)

for i in range(num_plots):
    graphs[i], = axes[i].plot([], [], 'o', c=color_seq[i] / 255.0)
    axes[i].set_xlim(-1.3, 1.3)
    axes[i].set_ylim(-1.3, 1.3)


def animate(i):
    freqs = s0.get_frequencies(offset + i, offset + i + freq_bins)
    freqs /= np.max(np.absolute(freqs))

    for i in range(num_plots):
        f_s = freq_ranges[i]
        f_e = freq_ranges[i + 1]
        graphs[i].set_data(freqs.real[f_s:f_e], freqs.imag[f_s:f_e])

    return fig


ani = animation.FuncAnimation(
    fig, animate, frames=120000, interval=10)

plt.show()
