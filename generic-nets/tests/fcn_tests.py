from networks.architectures.fcn import FCN
from networks.activations import relu
from networks.loss import squared_error
from scipy.io.wavfile import read, write

import matplotlib.pyplot as plt
import numpy as np

# sounds = '/Users/tru/Desktop/english/'
# sample_rate, data = read(sounds + 'understand.wav')


X = np.sin(440 * np.arange(1000))
y = X[::2]

X = X.reshape(1, -1)
y = y.reshape(1, -1)

layers = [X.shape[1], 500, y.shape[1]]
fcnn = FCN(layers=layers,
           X=X, y=y, activation=relu,
           loss=squared_error, lr=1e-6)
fcnn.train(iters=1000)
out = nn.predict(X)

plt.plot(X.reshape(-1))
plt.plot(out.reshape(-1))
plt.show()
