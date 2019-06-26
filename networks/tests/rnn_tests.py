from networks.architectures.rnn import RNN
from networks.activations import tanh
from networks.loss import squared_error
from scipy.io.wavfile import read, write

import matplotlib.pyplot as plt
import numpy as np

X = np.sin(440 * np.arange(1000))
y = X

X = X.reshape(1, -1)
y = y.reshape(1, -1)

sequence_len = 25
layers = [sequence_len, 100, 100, sequence_len]
rnn = RNN(layers=layers,
          X=X, y=y, activation=tanh,
          loss=squared_error, sequence_len=sequence_len, lr=1e-6)
rnn.forward()
rnn.backward()