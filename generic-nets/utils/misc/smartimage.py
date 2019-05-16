from scipy.ndimage import imread
from scipy.misc import imsave
from utils.misc import color, bound_check

import os


class SmartImage():

    def __init__(self, path):
        self.data = imread(path)
        self.bins = color.bins[self.to_ID_array()]

        self.rows = self.data.shape[0]
        self.cols = self.data.shape[1]
        self.channels = self.data.shape[2]

        self.path = os.path.splitext(path)[0]
        self.extension = os.path.splitext(path)[1]

    def reload(self):
        self.data = imread(self.path + self.extension)

    def in_bounds(self, r, c):
        return bound_check.in_bounds(self.data.shape, r, c)

    def to_ID_array(self):
        return self.data.dot(color.identifier)
