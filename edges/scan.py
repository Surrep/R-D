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

# setup for edge connection
angle_bins = np.linspace(pi / 2, -pi / 2, 12)
rows, cols = np.meshgrid(receptive_field, receptive_field)
angles = np.arctan(cols / rows)

print('loaded')


def find_spots(r, c):
    receptive_field = range(-1, 2)  # 3x3
    color = image[r, c]

    for r_off in receptive_field:
        for c_off in receptive_field:
            detect(color, r + r_off, c + c_off)


def detect(color, r, c):
    if image[r, c] != color:
        spots.add((r, c))
        out[r, c] = [255, 255, 255]


def connect(spot):
    r, c = spot

    receptive_field = np.arange(-3, 4)  # 7x7
    field = image[r + receptive_field, c + receptive_field]

    np.digitize(angles[field > 0], angle_bins)


def get_angle(r, c):
    return pi / 2 if not c else atan(r / c)


print('spotting')
start = time.time()

for r in range(1, rows - 1):
    for c in range(1, cols - 1):
        find_spots(r, c)

end = time.time()
print(end - start)
print(len(spots))

# print('edging')
# start = time.time()

# while len(spots):
#     connect(spots.pop())

# end = time.time()
# print(end - start)
# print(len(set(edges.values())))

# for edge in set(edges.values()):
#     color = np.random.randint(0, 256, (3))
#     for spot in edge.spots:
#         out[spot] = color


imsave('/Users/tru/Desktop/out22.jpg', out)
