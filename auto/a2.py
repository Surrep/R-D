from scipy.io.wavfile import read, write
import numpy as np

sounds = '/Users/tru/Desktop/english/'
sample_rate, data = read(sounds + 'four.wav')

print(*data.shape)

w0 = np.random.randn(*data.shape, 100)
a0 = data.dot(w0)

w1 = np.random.randn(100, *data.shape)
a1 = a0.dot(w1)

print(((a1 - data) ** 2).sum())
