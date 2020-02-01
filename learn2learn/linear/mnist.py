import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import AxesGrid


from mlxtend.data import loadlocal_mnist

# Get training data:
X, y = loadlocal_mnist(
    images_path='/Users/trumanpurnell/Workspace/bblabs/deep-blob/learn2learn/data/train-images-idx3-ubyte',
    labels_path='/Users/trumanpurnell/Workspace/bblabs/deep-blob/learn2learn/data/train-labels-idx1-ubyte')

X = X.astype(float) / 255

# Initialize the Weights: 10 Template Images which we will match against
weights = np.random.randn(784, 10)

# Train
alpha = 0.01
for i in range(100):
    error = 0
    for Xi, yi in zip(X[:1000], y[:1000]):
        prediction = weights.T.dot(Xi)
        prediction[yi] -= 1
        error += np.linalg.norm(prediction)
        gradient = Xi.reshape(-1, 1).dot(prediction.reshape(-1, 1).T)

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
