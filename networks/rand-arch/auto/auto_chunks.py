from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
import numpy as np
import math


class AutoRNN:

    def __init__(self, learning_rate, seq_len,
                 look_ahead, stride, lucidity):
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

    def generate(self, seed, num_samples):
        out = np.zeros((1, num_samples))
        out[:, :len(seed[0])] = seed

        for t in range(0, num_samples, self.stride):
            t_end = t + self.seq_len
            new_samples = out[:, t:t_end].dot(self.W1)
            if t_end + self.look_ahead > num_samples:
                break

            out[:, t_end:t_end + self.look_ahead] = new_samples

        return out

    def update_sequence(self, seq, pred, target, t_step):
        """ 
        We define a binomial distribution to represent the 'lucidity' of the model.
        This determines whether its own predictions shall be incorporated into future predictions (not lucid)
        or whether ground truth sequence will be used to make future predictions (lucid) 

        """

        p_dist = [self.lucidity, 1 - self.lucidity]
        choices = [False, True]  # false for target, true for self-generated
        mask = np.random.choice(a=choices, size=pred.shape, p=p_dist)

        t_cur = t_step + self.seq_len
        t_end = t_cur + self.look_ahead
        seq[:, t_cur:t_end] = np.where(mask, pred, target)

        return seq

    def fit(self, X, y, epsilon=1e-6, verbose=False):
        X = X.copy()
        cost = math.inf  # must begin to fit
        dW1 = np.zeros_like(self.W1)
        trials = 0

        while cost > epsilon:
            # update weights based on loss
            self.W1 -= self.learning_rate * dW1

            cost = 0
            # loop through input sequence
            for t in range(0, len(X[0]), self.stride):
                xt = self.get_samples(X, t, self.seq_len)
                yt = self.get_samples(y, t + self.seq_len, self.look_ahead)

                if xt is None or yt is None:  # we have reached end of sequence
                    break

                # get predictions
                zt = xt.dot(self.W1)

                # compute cost based on predictions
                cost += self.compute_cost(zt, yt)

                # propogate loss back to weights
                dy = zt - yt
                dW1 += xt.T.dot(dy)

                X = self.update_sequence(seq=X, pred=zt, target=yt, t_step=t)

            trials += 1
            if verbose:
                print(trials, cost)


sounds = '/Users/tru/Desktop/english/'
sample_rate, data = read(sounds + 'calc.wav')

X = (data.reshape(1, -1) / np.max(data))[:, 42000:143100]
y = X

arnn = AutoRNN(learning_rate=0.1, seq_len=25,
               look_ahead=150, stride=5, lucidity=1)

arnn.fit(X, y, epsilon=125, verbose=True)
out2 = arnn.generate(seed=X[:, :5], num_samples=10000)
