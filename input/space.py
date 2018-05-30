from scipy.misc import imread, imsave
import numpy as np


class Analyzer():

    def __init__(self, data):
        self.data = data

    def gen_slices(self, points):
        slices = np.array([self.data - point for point in points])
        differences = np.abs(slices).sum(axis=3)
        self.grouped_data = np.argmin(differences, axis=0)


img = imread('/Users/tru/Desktop/photos/fanfour.jpg')
slices = 5
a = Analyzer(img)
a.gen_slices(np.random.randint(0, 256, (slices, 3)))

[imsave('/Users/tru/Desktop/slices/slice{}.jpg'.format(s),
        s == a.grouped_data) for s in range(slices)]
