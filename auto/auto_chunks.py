from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
import numpy as np


def load_sound(path):
    sample_rate, data = read(path)
    data = data[:, 0].T

    return sample_rate, (data / np.max(data)).reshape(1, -1)


class AutoRNN:

    def __init__(self, learning_rate, sequence_len):
        self.learning_rate = learning_rate
        self.sequence_len = sequence_len
        self.W1 = np.random.randn(sequence_len, sequence_len)

    def predict(self, X):
        out = np.zeros_like(X)

        for t in range(len(X[0])):
            xt = self.get_samples(t)
            if xt is None:
                break
            zt = xt.dot(self.W1)
            out[:, t:t + sequence_len] = zt
            print(zt, 'zt')
            print(xt, 'xt')

        return out

    def get_samples(self, t, X):
        samples = X[:, t:t + self.sequence_len]
        return None if len(samples[0]) < self.sequence_len else return samples

    def compute_cost(self, yhat, y):
        return ((yhat - y) ** 2 / 2).sum()

    def fit(self, X, verbose=False):
        errors = []
        for t in range(len(X[0])):
            cost = 2  # inf

            if verbose:
                print('-----------------------------------', t)

            while cost > 1e-1:
                xt = self.get_samples(t, X)
                if xt is None:
                    break
                zt = xt.dot(W1)
                cost = compute_cost(zt, xt)
                errors.append(cost)

                if verbose:
                    print(cost)

                dy = zt - xt
                dW1 = xt.T.dot(dy)
                W1 -= learning_rate * dW1

        return np.array(errors)

