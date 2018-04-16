from scipy.io.wavfile import read, write
import numpy as np

sounds = '/Users/tru/Desktop/english/'
sample_rate, data = read(sounds + 'four.wav')

data = data.reshape(1, -1)
channels, samples = data.shape

# D_in is input dimension
# H is hidden dimension
# D_out is output dimension
D_in, H, D_out = samples, 100, samples
learning_rate = 0.001

# Auto encoder
x = data
y = data

# Randomly initialize weights
w1 = np.random.randn(D_in, H)
w2 = np.random.randn(H, D_out)

for itr in range(1000):
    # forward pass
    z1 = x.dot(w1)
    a1 = np.maximum(z1, 0)  # relu
    z2 = a1.dot(w2)

    # compute cost
    cost = np.square(z2 - y).sum() / 2
    if not itr % 25:
        print(cost)

    # backward pass
    dy = z2 - y
    dw2 = a1.T.dot(dy)
    da1 = dy.dot(w2.T)
    dz1 = da1.copy()
    dz1[z1 < 0] = 0
    dw1 = x.T.dot(dz1)

    w1 -= learning_rate * dw1
    w2 -= learning_rate * dw2
