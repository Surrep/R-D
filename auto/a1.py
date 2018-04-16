from scipy.io.wavfile import read, write
import numpy as np

sounds = '/Users/tru/Desktop/english/'
sample_rate, data = read(sounds + 'four.wav')
data = np.random.randn(10)

print(sample_rate, data.shape)


def recurrent_layer(data, weights):
    cp_data = np.zeros_like(data)
    cp_data[0] = data[0] * weights[0]
    for i in range(1, len(cp_data)):
        cp_data[i] = cp_data[i - 1] + data[i] * weights[i]

    return cp_data[1:]


def encoder(layers, data):
    al = data
    for l in range(layers):
        wl = np.random.randn(*al.shape)
        al = recurrent_layer(al, wl)

    return al


out = encoder(len(data) - 1, data)
print(out)

