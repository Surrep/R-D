from scipy.misc import imread, imsave
from collections import defaultdict
from edge import EdgeBox
from queue import Queue
from math import pi, atan

import pandas as pd
import numpy as np
import pickle
import time
import sys
import os
import shutil


sys.setrecursionlimit(1 << 30)
shutil.rmtree("/Users/tru/Desktop/slices/")
os.makedirs("/Users/tru/Desktop/slices/")


module, img_name, bins = sys.argv

print('loading bins')
color = int(bins) if bins else 2
bins = np.array(pd.read_csv(
    '/Users/tru/Workspace/surrep/recognition/data/colorBins{}.txt'.format(color), header=None)[0])
identifier = [256 ** 2, 256 ** 1, 256 ** 0]

original = imread('/Users/tru/Desktop/photos/' + img_name)
image = bins[original.dot(identifier)]
rows, cols = image.shape
out = np.zeros((rows, cols, 3))
spots = set()

edges = defaultdict(EdgeBox)
angle_bins = np.linspace(pi / 2, -pi / 2, 3)
print('loaded')


def find_spots(r, c):
    color = image[r, c]

    detect(color, r - 1, c)
    detect(color, r, c - 1)
    detect(color, r, c + 1)
    detect(color, r + 1, c)


def detect(color, r, c):
    if image[r, c] != color:
        spots.add((r, c))
        # out[r, c] = [255, 255, 255]


def connect(spot):
    spot_connector = Queue(len(spots))
    spot_connector.put(spot)
    receptive_field = (-2, 3)

    while spot_connector.qsize():
        spot = spot_connector.get()
        current_edge = edges[spot]

        angle = 0
        new_neighbors = []
        for r in range(*receptive_field):
            for c in range(*receptive_field):
                current_row, current_col = spot
                neighbor = (r + current_row, c + current_col)

                if neighbor in spots:
                    spots.discard(neighbor)
                    new_neighbors.append(neighbor)
                    spot_connector.put(neighbor)
                    angle += get_angle(r, c)

        if len(new_neighbors):
            angle = np.digitize(angle / len(new_neighbors), angle_bins)
            if current_edge.is_oriented_along(angle):
                for neighbor in new_neighbors:
                    current_edge.absorb(*neighbor)
                    edges[neighbor] = current_edge


def get_angle(r, c):
    sign = 1 if r >= 0 else -1
    return sign * pi / 2 if not c else atan(r / c)


print('spotting')
start = time.time()

for r in range(1, rows - 1):
    for c in range(1, cols - 1):
        find_spots(r, c)

end = time.time()
print(end - start)
print(len(spots))

print('edging')
start = time.time()

while len(spots):
    connect(spots.pop())

end = time.time()
print(end - start)
print(len(set(edges.values())))

for edge in set(edges.values()):
    color = np.random.randint(0, 256, (3))
    for spot in edge.spots:
        out[spot] = color


imsave('/Users/tru/Desktop/out23.jpg', out)
