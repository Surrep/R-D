from sklearn.datasets import fetch_mldata
from math import sin, pi
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
        np.random.randn(dims[i], dims[i + 1]) * 0.2
        for i in range(len(dims) - 1)
    ]


W = init_weights([28, 2] + [int(sin(l) * 50)
                            for l in np.arange(0.2, pi, 4 / 17)] + [1])


samples = 250
points = np.zeros((samples, 2))
rand_idxs = np.random.choice(np.arange(70000), size=samples, replace=False)

imgs = mnist.data[rand_idxs]
clrs = mnist.target[rand_idxs]

for i, img in enumerate(imgs):
    img = img.reshape(28, 28)
    points[i] = forward(img, W).reshape(2)


plt.scatter(points[:, 0], points[:, 1], c=clrs)
plt.show()

