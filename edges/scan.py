from scipy.misc import imread, imsave
from collections import defaultdict
from edge import EdgeBox
from math import pi, atan
from colors import binitize

import numpy as np
import pickle
import time
import sys
import os
import shutil


sys.setrecursionlimit(1 << 30)
shutil.rmtree("/Users/tru/Desktop/slices/")
os.makedirs("/Users/tru/Desktop/slices/")


module, img_name = sys.argv

print('loading image')

image = binitize(imread('/Users/tru/Desktop/photos/{}.jpg'.format(img_name)))
rows, cols = image.shape
out = np.zeros((rows, cols, 3))

spots = set()
edges = defaultdict(EdgeBox)

print('loaded')


def find_spots():
    receptive_field = range(-1, 2)  # 3x3

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            color = image[r, c]

            for r_off in receptive_field:
                for c_off in receptive_field:
                    if image[r + r_off, c + c_off] != color:
                        spots.add((r, c))
                        # out[r, c] = [255, 255, 255]


def find_edges():
    receptive_field = np.arange(-3, 4)  # 7x7
    rows, cols = np.meshgrid(receptive_field, receptive_field)
    angles = np.arctan(cols / rows)
    angle_bins = np.linspace(1.5, -1.5, 12)

    while len(spots):
        r, c = spots.pop()
        field = image[r + receptive_field, c + receptive_field]

        np.digitize(angles[field > 0], angle_bins) % 12


print('--------spotting----------')
start = time.time()
find_spots()
end = time.time()
print(end - start)
print(len(spots))

print('--------edging-----------')
start = time.time()
find_edges()
end = time.time()
print(end - start)


imsave('/Users/tru/Desktop/out22.jpg', out)
