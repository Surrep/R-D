from sklearn.datasets import fetch_mldata
from scipy.misc import imread, imsave
from image import get_colors


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(suppress=True, linewidth=1000, threshold=np.nan)


class Analyzer():

    def __init__(self, data, points):
        self.data = data
        self.points = points

        self.diffs = np.array([self.data - point for point in points])
        self.sqr_diffs = np.square(self.diffs).sum(axis=3)
        self.binned_data = np.argmin(self.sqr_diffs, axis=0)
        self.slices = np.array(
            [self.binned_data == bin for bin in range(len(self.points))]
        ).astype(np.int)



img = imread('/Users/tru/Desktop/bet.jpg')
points = get_colors(2, 2, 2)

a = Analyzer(img, points)

# for i, s in enumerate(a.slices):
#     imsave('/Users/tru/Desktop/slices/im{}.jpg'.format(i), s)

imsave('/Users/tru/Desktop/flam.jpg', a.binned_data)
