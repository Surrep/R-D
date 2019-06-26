from scipy.io.wavfile import read, write

import matplotlib.pyplot as plt
import numpy as np

sounds = '/Users/tru/Desktop/english/'
sample_rate, data = read(sounds + 'four.wav')

# Auto encoder
x = np.sin(np.arange(300).reshape(1, -1))
y = x

# D_in is input dimension; H are hidden dimensions; D_out is output dimension
D_in, H1, H2 D_out = x.shape[1], 100, 100, x.shape[1]
learning_rate = 9e-6

# Randomly initialize weights
w1 = np.random.randn(D_in, H1)
w2 = np.random.randn(H1, H2)
w3 = np.random.randn(H2, D_out)

for itr in range(7500):
    # forward pass
    z1 = x.dot(w1)
    a1 = np.maximum(z1, 0)  # relu
    z2 = a1.dot(w2)
    a2 = np.maximum(z2, 0)  # relu
    z3 = a2.dot(w3)

    # compute cost
    cost = np.square(z3 - y).sum() / 2

    # backward pass
    dy = z2 - y
    dw2 = a1.T.dot(dy)
    da1 = dy.dot(w2.T)
    dz1 = da1.copy()
    dz1[z1 < 0] = 0
    dw1 = x.T.dot(dz1)

    w1 -= learning_rate * dw1
    w2 -= learning_rate * dw2


plt.plot(x[0])
plt.plot(ans[0])
plt.show()
