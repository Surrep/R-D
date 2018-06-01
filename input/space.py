from sklearn.datasets import fetch_mldata
from scipy.misc import imread, imsave
from scipy.stats import mode

import numpy as np
np.set_printoptions(suppress=True, linewidth=1000, threshold=np.nan)


class Analyzer():

    def __init__(self, data):
        self.data = data

    def gen_slices(self, points):
        slices = np.array([self.data - point for point in points])
        differences = np.abs(slices).sum(axis=3)
        self.grouped_data = np.argmin(differences, axis=0)


mnist = fetch_mldata('MNIST original')
img = imread('/Users/tru/Desktop/photos/whop.jpg')
# img = mnist.data[0].reshape(28, 28)

slices = 16
dims = 3
base = 256
a = Analyzer(img)

points = np.linspace(0, base ** 3, slices)
points = np.flip(np.array([points // base ** i %
                           base for i in range(dims)]).T, 1)[:-1]

a.gen_slices(points)
[imsave('/Users/tru/Desktop/slices/grups{}.jpg'.format(i),
        a.grouped_data == i) for i in range(slices)]
