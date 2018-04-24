from scipy.io.wavfile import read, write
import numpy as np

sounds = '/Users/tru/Desktop/english/'
sample_rate, data = read(sounds + 'four.wav')

print(sample_rate, data.shape)

sequence_len = 10
learning_rate = 1e-1

X = np.sin(880 * np.arange(2000)).reshape(1, -1)
WI = np.random.randn(sequence_len, sequence_len)


def forward_layer(prev, weights):
    return prev.dot(weights)


def compute_cost(yhat, y):
    return ((yhat - y) ** 2 / 2).sum()


def get_samples(data, t, sequence_len):
    samples = data[:, t:t + sequence_len]
    num_samples = len(samples[0])
    padding = np.repeat(0, sequence_len - num_samples)

    return np.append(samples, padding).reshape(1, -1)


for t in range(len(X[0])):
    cost = 2  # inf
    # print('-----------------------------------', t)
    while cost > 1e-5:
        xt = get_samples(X, t, sequence_len)
        zt = forward_layer(xt, WI)
        cost = compute_cost(zt, xt)

        # print(cost)

        dy = zt - xt
        dWI = xt.T.dot(dy)
        WI -= learning_rate * dWI

