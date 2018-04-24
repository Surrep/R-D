from scipy.io.wavfile import read, write
import numpy as np


def load_sound(path):
    sample_rate, data = read(path)
    data = data[:, 0].T

    return sample_rate, (data / np.max(data)).reshape(1, -1)


def forward_layer(prev, weights):
    return prev.dot(weights)


def compute_cost(yhat, y):
    return ((yhat - y) ** 2 / 2).sum()


def get_samples(data, t, sequence_len):
    samples = data[:, t:t + sequence_len]
    if len(samples[0]) is not sequence_len:
        return None

    return samples


def fit(X, sequence_len, W1, learning_rate, verbose=False):
    for t in range(len(X[0])):
        cost = 2  # inf

        if verbose:
            print('-----------------------------------', t)

        while cost > 1e-1:
            xt = get_samples(X, t, sequence_len)
            if xt is None:
                break
            zt = forward_layer(xt, W1)
            cost = compute_cost(zt, xt)

            if verbose:
                print(cost)

            dy = zt - xt
            dW1 = xt.T.dot(dy)
            W1 -= learning_rate * dW1


sounds = '/Users/tru/Desktop/english/'
sample_rate1, data1 = load_sound(sounds + 'tru1.wav')

sequence_len = 10
learning_rate = 1e-1

X = data1
W1 = np.random.randn(sequence_len, sequence_len)

fit(X, sequence_len, W1, learning_rate, verbose=False)
