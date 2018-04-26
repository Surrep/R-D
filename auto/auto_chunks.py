from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
import numpy as np
import math


def load_sound(path):
    sample_rate, data = read(path)
    data = data[:, 0].T

    return sample_rate, (data / np.max(data)).reshape(1, -1)


class AutoRNN:

    def __init__(self, learning_rate, seq_len, look_ahead,
                 stride, lucidity):
        self.lucidity = lucidity
        self.learning_rate = learning_rate
        self.seq_len = seq_len
        self.look_ahead = look_ahead
        self.stride = stride

        self.W1 = np.random.randn(seq_len, look_ahead) * 0.01

    def get_samples(self, data, t, num_samples):
        return None if len(data[0]) < (t + num_samples) else data[:, t:t + num_samples]

    def compute_cost(self, yhat, y):
        return ((yhat - y) ** 2 / 2).sum()

    def fit(self, X, y, epsilon=1e-5, cap=500, verbose=False):
        X = X.copy()  # copy data so as not to mutate original

        # loop through entire sequence
        for t in range(0, len(X[0]), self.stride):

            xt = self.get_samples(X, t, self.seq_len)
            yt = self.get_samples(y, t + self.seq_len, self.look_ahead)

            if xt is None or yt is None:  # we have reached end of sequence
                return

            cost = math.inf  # cost is inf before training
            count = 0  # attempts to minimize loss
            attempts_exhausted = False  # true if we take too long to minimize error

            # attempt to minimize distance between predictions and true sample
            while cost > epsilon and not attempts_exhausted:
                # get predictions
                zt = xt.dot(self.W1)

                # compute cost based on predictions
                cost = self.compute_cost(zt, yt)

                # propogate loss back to weights
                dy = zt - yt
                dW1 = xt.T.dot(dy)

                # update weights based on loss
                self.W1 -= self.learning_rate * dW1

                # check for terminating conditions
                count += 1
                attempts_exhausted = count > cap

            p_dist = [self.lucidity, 1 - self.lucidity]
            choices = [False, True]
            mask = np.random.choice(a=choices, size=zt.shape, p=p_dist)

            start = t + self.seq_len
            end = start + self.look_ahead
            if (end - start) == self.seq_len:
                X[:, start:end] = np.where(mask, zt, xt)

            if verbose and not t % 1e3:
                print(t, count, cost)


sounds = '/Users/tru/Desktop/english/'
sample_rate, data = read(sounds + 'calc.wav')

X = (data.reshape(1, -1) / np.max(data))[:, 55000:57000]
y = X

arnn = AutoRNN(learning_rate=0.1, seq_len=10,
               look_ahead=10, stride=10, lucidity=0)

errors = arnn.fit(X, y, epsilon=1e-13, cap=1000, verbose=True)

out2 = arnn.generate(X[:, :10], 1900)
