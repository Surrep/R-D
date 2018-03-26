from scipy.misc import imread, imsave
from edge import EdgeBox
from math import pi, atan, floor
from colors import binitize, random_color

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
edges = dict()

angle_bin_count = 256
angle_bins = np.linspace(pi / 2, -pi / 2, angle_bin_count)

print('loaded')


def find_spots():
    receptive_field = range(-1, 2)  # 3x3

    for r in range(5, rows - 5):
        for c in range(5, cols - 5):
            color = image[r, c]

            for r_off in receptive_field:
                for c_off in receptive_field:
                    if image[r + r_off, c + c_off] != color:
                        spots.add((r, c))
                        # out[r, c] = [255, 255, 255]


def find_edges():
    receptive_field = np.arange(-3, 4)
    angle_rows, angle_cols = np.meshgrid(receptive_field, receptive_field)
    angles = np.arctan2(angle_cols, angle_rows)

    while len(spots):
        r, c = spots.pop()
        field = image[np.ix_(r + receptive_field, c + receptive_field)]

        edge_pixels = (field == 0).nonzero()
        angle = np.digitize(angles[edge_pixels].mean(), angle_bins)

        for (r_off, c_off) in zip(*edge_pixels):
            spot = (r + r_off, c + c_off)
            spots.discard(spot)

            if spot not in edges:
                edges[spot] = angle


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

color_pallete = [random_color() for i in range(angle_bin_count + 1)]

for spot in edges:
    out[spot] = color_pallete[edges[spot]]


imsave('/Users/tru/Desktop/out.jpg', out)
