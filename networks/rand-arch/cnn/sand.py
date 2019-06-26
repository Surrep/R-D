from sklearn.datasets import fetch_mldata
from math import sin, pi, tan, cos, inf
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt
import numpy as np

mnist = fetch_mldata('MNIST original')


def forward(image, layers):
    al = image
    for l in layers:
        al = al.dot(l)

    return al


def init_weights(dims):
    return [
        np.random.randn(dims[i], dims[i + 1]) * 0.1
        for i in range(len(dims) - 1)
    ]


samples = 15000
dims = 3
start = 30000
points = np.zeros((samples, dims))
layers = init_weights(
    [784, 100, 50, 25, 12, 10, 9, 8, 7, 6, 5, dims])

targets = mnist.target[start:start + samples]
clusters = np.unique(targets)
print(clusters)

for i, image in enumerate(mnist.data[start:start + samples]):
    points[i] = forward(image.reshape(1, -1), layers)

# points = np.random.randn(784, dims)
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')


kmeans = KMeans(n_clusters=len(clusters), random_state=0).fit(points)

print(kmeans.cluster_centers_)


plt.scatter(points[:, 0], points[:, 1], c=targets)
plt.show()
