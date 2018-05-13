from sklearn.datasets import fetch_mldata
from math import sin, pi, tan, cos, inf
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

mnist = fetch_mldata('MNIST original')


def forward(image, layers):
    al = image
    for l in layers:
        al = np.tanh(al.dot(l))

    return al


def init_weights(dims):
    return [
        np.random.randn(dims[i], dims[i + 1]) * 0.4
        for i in range(len(dims) - 1)
    ]


samples = 1000
dims = 3
start = 40000
points = np.zeros((samples, dims))
W = np.random.rand(784, dims)

print(np.unique(mnist.target[start:start + samples]))

for i, image in enumerate(mnist.data[start:start + samples]):
    points[i] = image.dot(W)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2])
plt.show()
