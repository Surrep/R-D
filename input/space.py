from sklearn.datasets import fetch_mldata
from scipy.misc import imread, imsave
from scipy.stats import mode


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(suppress=True, linewidth=1000, threshold=np.nan)


class Analyzer():

    def __init__(self, data, points):
        self.data = data
        self.points = points

        self.differences = np.array([self.data - point for point in points])
        self.abs_differences = np.abs(self.differences).sum(axis=3)
        self.binned_data = np.argmin(self.abs_differences, axis=0)
        self.slices = np.array(
            [self.binned_data == bin for bin in range(len(self.points))]
        ).astype(np.int)


# mnist = fetch_mldata('MNIST original')
img = imread('/Users/tru/Desktop/photos/bord.jpg')
# img = mnist.data[0].reshape(1, -1)
# points = np.linspace(0, base ** 3, slices)
# points = np.flip(np.array([points // base ** i %
#                            base for i in range(dims)]).T, 1)[:-1]

rd = img.reshape(-1, 3)
print(rd)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter(rd[:, 0], rd[:, 1], rd[:, 2])
plt.show()

# plt.imshow(img[400:450, 400:450])
# plt.show()
# slices = 2
# dims = 3s
# base = 256

# points = np.random.randint(0, base, (slices, dims))
# img = np.random.randint(0, 256, (3, 3, 3))
# a = Analyzer(img, points)
