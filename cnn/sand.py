from sklearn.datasets import fetch_mldata
from math import sin, pi, tan, cos
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

mnist = fetch_mldata('MNIST original')


def forward(image, layers):
    dim_layer, *rest = layers
    al = image.dot(dim_layer).T

    for l in layers:
        al = al.dot(l)

    return al


def init_weights(dims):
    return [
        np.random.randn(dims[i], dims[i + 1]) * 0.1
        for i in range(len(dims) - 1)
    ]


mid = [int(sin(l) * 50) for l in np.linspace(0.1, pi - 0.1, 10)]
W = init_weights([28, 3] + mid + [1])


samples = 5000
points = np.zeros((samples, 3))
rand_idxs = np.random.choice(np.arange(70000), size=samples, replace=False)

imgs = mnist.data[rand_idxs]
clrs = mnist.target[rand_idxs]

for i, img in enumerate(imgs):
    img = img.reshape(28, 28)
    points[i] = forward(img, W).reshape(3)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=clrs)

plt.show()
