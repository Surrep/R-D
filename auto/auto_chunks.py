from scipy.io.wavfile import read, write
import numpy as np

sounds = '/Users/tru/Desktop/english/'
sample_rate, data = read(sounds + 'four.wav')

print(sample_rate, data.shape)

sequence_len = 10
learning_rate = 1e-1

X = np.sin(880 * np.arange(50)).reshape(1, -1)
WI = np.random.randn(sequence_len, sequence_len)

for t in range(len(X[0])):
    cost = 2  # inf
    print('-----------------------------------', t)
    while cost > 1e-8:
        xt = X[:, t:t + sequence_len]
        if xt.shape[1] != sequence_len:
            break

        zt = xt.dot(WI)

        cost = ((zt - xt) ** 2 / 2).sum()
        print(cost)

        dy = zt - xt
        dWI = xt.T.dot(dy)

        WI -= learning_rate * dWI
