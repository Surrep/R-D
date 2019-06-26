from sklearn.datasets import fetch_mldata
from math import sin, pi, tan, cos, inf
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

mnist = fetch_mldata('MNIST original')

maps = 30
rows = cols = 28
filter_size = 3
margin = 5
stride = 8
samples = 1500
dims = 3

L1 = np.random.rand(filter_size, filter_size, 1, maps)
receptive_field = np.arange(-1, 2)
out = np.zeros((samples, rows, cols, maps))


rand_idxs = np.random.choice(np.arange(70000), size=samples, replace=False)


imgs = mnist.data[rand_idxs]
clrs = mnist.target[rand_idxs]

for im, img in enumerate(imgs):
    img = img.reshape(rows, cols)

    for r in range(margin, rows - margin, stride):
        for c in range(margin, cols - margin, stride):
            for i in range(maps):
                field = np.ix_(receptive_field + r, receptive_field + c)

                activation = img[field] * L1[:, :, :, i]
                out[im, r, c, i] = activation.sum()

points = np.zeros((samples, dims))
L2 = np.random.rand(rows * cols * maps, dims)
for im, img in enumerate(out):
    points[im] = img.reshape(1, rows * cols * maps).dot(L2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=clrs)
plt.show()
