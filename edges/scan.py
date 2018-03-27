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

angle_bin_count = 6
angle_bins = np.linspace(pi, 0, angle_bin_count)

print('loaded')


def find_spots():
    receptive_field = range(-1, 2)  # 3x3

    for r in range(2, rows - 2):
        for c in range(2, cols - 2):
            color = image[r, c]

            for r_off in receptive_field:
                for c_off in receptive_field:
                    if image[r + r_off, c + c_off] != color:
                        spots.add((r, c))
                        out[r, c] = [255, 255, 255]


def find_edges():
    receptive_field = np.arange(-2, 3)

    while len(spots):
        r, c = spots.pop()
        cur_edge = edges[(r, c)]

        angles = []
        for r_off in receptive_field:
            for c_off in receptive_field:
                spot = (r + r_off, c + c_off)
                if spot in spots:
                    spots.discard(spot)
                    cur_edge.absorb(*spot)
                    angles.append(np.arctan2(c_off, r_off) % pi)
                    edges[spot] = cur_edge

        cur_edge.orientation = int(np.digitize(np.mean(angles), angle_bins))


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
    if edges[spot].orientation:
        out[spot] = color_pallete[edges[spot].orientation]


imsave('/Users/tru/Desktop/out24.jpg', out)
