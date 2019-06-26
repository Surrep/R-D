from scipy import signal
from resource import Resource
from imageio import imread, imsave
from scipy.io.wavfile import read, write

import numpy as np
import matplotlib.pyplot as plt

sound_uri = Resource(('../data/sounds/', 'greetings', 'wav'))
rate, channels = read(sound_uri.string)
band_count = 50

sound = channels[:, 0].reshape(-1)
sound = sound - np.mean(channels)
sound = sound / np.max(sound)

f, t, Sxx = signal.spectrogram(sound, rate)
# plt.pcolormesh(t, f, Sxx)
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()

# window = 129 * 2
# sample_total = len(sound) - window
# sample_frames = sample_total // window + 1

# freqs = np.zeros((sample_frames, window // 2 + 1)).astype(complex)
# replica = np.zeros_like(sound)

# for i, sample in enumerate(range(0, sample_total, window)):
#     time = np.arange(sample, sample+window)
#     time = np.tile(time, band_count).reshape(-1, time.size)

#     freqs[i] = np.fft.rfft(sound[sample:sample+window])
#     power_spectrum = np.abs(freqs[i]) ** 2

#     dominants = np.argsort(power_spectrum)[-band_count:].reshape(band_count, 1)
#     pure_tones = np.sin(time * dominants * 2 * np.pi)

#     replica[sample:sample+window] = pure_tones.sum(axis=0)

# write('fuzzy.wav', rate, replica / replica.max())

# fuzzy_uri = Resource(('./', 'fuzzy', 'wav'))
# rate, channels = read(fuzzy_uri.string)

# plt.plot(channels)
# plt.show()
