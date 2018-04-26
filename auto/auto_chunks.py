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

            # after the prediction is made (zt), we incorporate it into our signal
            X = self.update_sequence(seq=X, pred=zt, target=yt, t_step=t)

            if verbose and not t % 1e3:
                print(t, count, cost)

