from scipy.misc import imread, imsave
from collections import defaultdict
from shape import Shape
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
        out[r, c] = [255, 255, 255]


rng = 1

print('seeing')
start = time.time()

for r in range(rng, rows - rng, 1):
    for c in range(rng, cols - rng, 1):
        find_spots(r, c)


end = time.time()
print(end - start)


DIR = {
    'N': pi / 2,
    'NE': pi / 4,
    'E': 0,
    'SE': - pi / 4,
}


def connect():
    neighbors = Queue(len(spots))
    neighbors.put(spots.pop())
    edges = defaultdict(Edge)

    while neighbors.qsize():
        r, c = neighbors.get()
        current_edge = edges[(r, c)]
        old_neighbors_size = neighbors.qsize()
        sum_angle = 0

        sum_angle += follow_neighbor(neighbors, (r - 1, c - 1), DIR['SE'])
        sum_angle += follow_neighbor(neighbors, (r - 1, c), DIR['N'])
        sum_angle += follow_neighbor(neighbors, (r - 1, c + 1), DIR['NE'])

        sum_angle += follow_neighbor(neighbors, r, c - 1, DIR['E'])
        sum_angle += follow_neighbor(neighbors, r, c + 1, DIR['E'])

        sum_angle += follow_neighbor(neighbors, (r + 1, c - 1), DIR['NE'])
        sum_angle += follow_neighbor(neighbors, (r + 1, c), DIR['N'])
        sum_angle += follow_neighbor(neighbors, (r + 1, c + 1), DIR['SE'])

        net_direction = sum_angle / (neighbors.qsize() - old_neighbors_size)

        if current_edge.is_oriented_along(net_direction):
            current_edge.absorb(r, c)


def follow_neighbor(neighbors, neighbor, direction):
    if neighbor in spots:
        spots.discard(neighbor)
        neighbors.put(neighbor)
        return direction

    return 0

    # start = time.time()
    # print('processing', len(spots))
    # i = 0
    # while len(spots):
    #     shape = connect(Shape(), *next(iter(spots)))
    #     if shape.area() > 10:
    #         imsave('/Users/tru/Desktop/slices/try{}.jpg'.format(i),
    #                original[shape.index_tuple()])
    #         i += 1
    # end = time.time()
    # print(end - start)


imsave('/Users/tru/Desktop/out{}.jpg'.format(color), out)
