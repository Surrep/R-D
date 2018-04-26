from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
import numpy as np
import math


def load_sound(path):
    sample_rate, data = read(path)
    data = data[:, 0].T

    return sample_rate, (data / np.max(data)).reshape(1, -1)


class AutoRNN:

    def __init__(self, learning_rate, sequence_len, look_ahead,
                 stride, lucidity):
        self.lucidity = lucidity
        self.learning_rate = learning_rate
        self.sequence_len = sequence_len
        self.look_ahead = look_ahead
        self.stride = stride
        self.W1 = np.random.randn(sequence_len, sequence_len) * 0.01

    def predict(self, X):
        X = X.copy()
        out = np.zeros_like(X)
        for t in range(0, len(X[0]), self.stride):
            xt = self.get_samples(X, t)
            if xt is None:
                break
            zt = xt.dot(self.W1)
            out[:, t:t + self.sequence_len] = zt

        return out

    def generate(self, seed, time_steps):
        out = np.zeros((1, time_steps * self.sequence_len))

        for t in range(0, time_steps, self.stride):
            print(seed.round(3))
            seed = seed.dot(self.W1)
            print(seed.round(3))
            out[:, t:t + self.sequence_len] = seed
            print('--------------------------')

        return out

    def get_samples(self, data, t):
        samples = data[:, t:t + self.sequence_len]
        return None if len(samples[0]) < self.sequence_len else samples

    def compute_cost(self, yhat, y):
        return ((yhat - y) ** 2 / 2).sum()

    def fit(self, X, y, epsilon=1e-5, cap=500, verbose=False):
        X = X.copy()
        for t in range(0, len(X[0]), self.stride):
            cost = math.inf
            end_sequence = False
            attempts_exhausted = False
            count = 0  # attempts to minimize loss

            while cost > epsilon and not attempts_exhausted and not end_sequence:
                xt = self.get_samples(X, t)
                yt = self.get_samples(y, t + self.look_ahead)

                end_sequence = xt is None or yt is None

                if not end_sequence:
                    zt = xt.dot(self.W1)
                    cost = self.compute_cost(zt, yt)
                    dy = zt - yt
                    dW1 = xt.T.dot(dy)

                    self.W1 -= self.learning_rate * dW1

                    count += 1
                    attempts_exhausted = count > cap

            if not end_sequence:
                p_dist = [self.lucidity, 1 - self.lucidity]
                choices = [False, True]
                mask = np.random.choice(a=choices, size=zt.shape, p=p_dist)

                start = t + self.look_ahead
                end = start + self.sequence_len
                if (end - start) == self.sequence_len:
                    X[:, start:end] = np.where(mask, zt, xt)

            if verbose and not t % 1e3:
                print(t, count, cost)


sounds = '/Users/tru/Desktop/english/'
sample_rate, data = read(sounds + 'calc.wav')

X = (data.reshape(1, -1) / np.max(data))[:, 55000:57000]
y = X

arnn = AutoRNN(learning_rate=0.1, sequence_len=10,
               look_ahead=10, stride=10, lucidity=0)

errors = arnn.fit(X, y, epsilon=1e-13, cap=1000, verbose=True)

out2 = arnn.generate(X[:, :10], 1900)
