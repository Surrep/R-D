from scipy.io.wavfile import read, write
import numpy as np

sounds = '/Users/tru/Desktop/english/'
sample_rate, data = read(sounds + 'four.wav')


sequence_len = 10
learning_rate = 1e-1
samples = 30

X = np.sin(880 * np.arange(samples)).reshape(1, -1)
W1 = np.random.randn(sequence_len, sequence_len)


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

        while cost > 1e-5:
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


fit(X, sequence_len, W1, learning_rate, verbose=True)

