import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.axes_grid1 import AxesGrid
from keras.datasets import mnist

# Get training data:
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalize images
test_images = X_test.reshape(-1, 784) / 255
train_images = X_train.reshape(-1, 784) / 255

# One-hot encode labels
y_train_hot = np.zeros((y_train.size, 10))
y_train_hot[np.arange(y_train.size), y_train] = 50

y_test_hot = np.zeros((y_test.size, 10))
y_test_hot[np.arange(y_test.size), y_test] = 50

# Assign one-hot labels
test_labels = y_test_hot
train_labels = y_train_hot

# Initialize the Weights: 10 Template Images which we will match against
weights = 0.2 * np.random.random((784, 10)) - 0.1

# Train
alpha = 0.0000001
for i in range(100):
    predictions = train_images.dot(weights)
    deltas = predictions - train_labels
    error = np.linalg.norm(deltas)
    gradient = train_images.T.dot(deltas)

    weights -= alpha * gradient

    if not (i % 10):
        print(error)

# Display Template Images
fig = plt.figure(figsize=(10, 10))

grid = AxesGrid(fig, 111,
                nrows_ncols=(2, 5),
                cbar_mode='single',
                cbar_location='top',
                cbar_pad=0.1)

for i, ax in enumerate(grid):
    ax.set_axis_off()
    im = ax.imshow(weights.T[i].reshape(28, 28))

cbar = ax.cax.colorbar(im)
plt.show()
