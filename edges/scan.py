from scipy.misc import imread, imsave
from edge import EdgeBox
from collections import defaultdict
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
image_path = '/Users/tru/Desktop/photos/{}.jpg'.format(img_name)

image = binitize(imread(image_path))
rows, cols = image.shape
out = np.zeros((rows, cols, 3))

spots = set()
edges = defaultdict(EdgeBox)

angle_bin_count = 8
angle_bins = np.linspace(pi / 2, -pi / 2, angle_bin_count)

print('loaded')


def find_spots():
    receptive_field = range(-1, 2)  # 3x3

    for r in range(10, rows - 10):
        for c in range(10, cols - 10):
            color = image[r, c]

            for r_off in receptive_field:
                for c_off in receptive_field:
                    if image[r + r_off, c + c_off] != color:
                        spots.add((r, c))
                        # out[r, c] = [255, 255, 255]


def find_edges():
    receptive_field = np.arange(-4, 5)
    angle_rows, angle_cols = np.meshgrid(receptive_field, receptive_field)
    angles = np.arctan2(angle_cols, angle_rows)

    while len(spots):
        r, c = spots.pop()
        current_edge = edges[(r, c)]
        field = image[np.ix_(r + receptive_field, c + receptive_field)]

        edge_pixels = (field).nonzero()
        angle = int(np.digitize(angles[edge_pixels].mean(), angle_bins))
        current_edge.orientation = angle

        for (r_off, c_off) in zip(*edge_pixels):
            spot = (r + r_off, c + c_off)
            spots.discard(spot)
            edges[spot] = current_edge


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
print(len(set(edges.values())))

color_pallete = [random_color() for i in range(angle_bin_count + 1)]

for spot in edges:
    if not edges[spot].orientation:
        print(spot, ' has no orientation')
        continue

    out[spot] = color_pallete[edges[spot].orientation]


imsave('/Users/tru/Desktop/out24.jpg', out)
