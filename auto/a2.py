from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
import numpy as np

sounds = '/Users/tru/Desktop/english/'
sample_rate, data = read(sounds + 'four.wav')

# Auto encoder
x = np.sin(np.arange(20).reshape(1, -1))
y = x

# D_in is input dimension
# H is hidden dimension
# D_out is output dimension
D_in, H, D_out = x.shape[1], 19, x.shape[1]
learning_rate = 1e-3

# Randomly initialize weights
w1 = np.random.randn(D_in, H)
w2 = np.random.randn(H, D_out)

ans = None
for itr in range(100):
    # forward pass
    z1 = x.dot(w1)
    a1 = np.maximum(z1, 0)  # relu
    z2 = a1.dot(w2)

    ans = z2
    # compute cost
    cost = np.square(z2 - y).sum() / 2
    print(cost)

    # backward pass
    dy = z2 - y
    dw2 = a1.T.dot(dy)
    da1 = dy.dot(w2.T)
    dz1 = da1.copy()
    dz1[z1 < 0] = 0
    dw1 = x.T.dot(dz1)

    # print(np.linalg.norm(x), 'x')
    # print(np.linalg.norm(w1), 'w1')
    # print(np.linalg.norm(z1), 'z1')
    # print(np.linalg.norm(a1), 'a1')

    # print(y, 'y')
    # print(dy, 'dy')
    # print(dw2[0, :2])
    # print(da1[0, :2])
    # print(dz1[0, :2])
    # print(dw1[0, :2])
    # print('------------------')

    w1 -= learning_rate * dw1
    w2 -= learning_rate * dw2


plt.plot(x[0])
plt.plot(ans[0])
plt.show()
