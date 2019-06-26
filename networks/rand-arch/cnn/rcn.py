from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
import numpy as np
import math


class AutoRNN:

    def __init__(self, learning_rate, neuron_count):
        self.learning_rate = learning_rate
        self.neuron_count = neuron_count

        while neuron_count > 1:
            chunk = np.random.randint(0, neuron_count)
            cluster = np.random.randn(1, chunk)
            neuron_count -= chunk
            print(neuron_count)


arnn = AutoRNN(learning_rate=0.01, neuron_count=7000)

# sounds = '/Users/tru/Desktop/english/'
# sample_rate, data = read(sounds + 'calc.wav')

# X = (data.reshape(1, -1) / np.max(data))[:, 42000:143100]
# y = X

# arnn = AutoRNN(learning_rate=0.01, seq_len=10,
#                look_ahead=20, stride=10, lucidity=0,
#                filters=1)

# arnn.fit(X, y, epsilon=1e-6, verbose=True)
