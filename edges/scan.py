from scipy.misc import imread, imsave
from shape import Shape
import pandas as pd
import numpy as np
import pickle
import time
import sys
import os
import shutil
from math import pi, atan

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
edges = set()

print('loaded')


def find_edges(r, c):
    color = image[r, c]

    detect(color, r - 1, c)
    detect(color, r, c - 1)
    detect(color, r, c + 1)
    detect(color, r + 1, c)


def detect(color, r, c):
    if image[r, c] != color:
        edges.add((r, c))
        out[r, c] = [255, 255, 255]


rng = 1

print('seeing')
start = time.time()

for r in range(rng, rows - rng, 1):
    for c in range(rng, cols - rng, 1):
        find_edges(r, c)


end = time.time()
print(end - start)

print('angles')


def connect():
    # edge = edges.pop()
    # while len(edges):
    # r, c = edge
    r = 32
    c = 54

    sum_angle = 0
    neighbors = []
    for r_off in range(-1, 2):
        for c_off in range(-1, 2):
            neighbor = (r + r_off, c + c_off)
            if neighbor in edges:
                neighbors.append(neighbor)
                sum_angle += pi / 2 if not c_off else atan(r_off / c_off)

    print(180 * sum_angle / pi / len(neighbors))

    # return shape


connect()
# start = time.time()
# print('processing', len(edges))
# i = 0
# while len(edges):
#     shape = connect(Shape(), *next(iter(edges)))
#     if shape.area() > 10:
#         imsave('/Users/tru/Desktop/slices/try{}.jpg'.format(i),
#                original[shape.index_tuple()])
#         i += 1
# end = time.time()
# print(end - start)


imsave('/Users/tru/Desktop/out{}.jpg'.format(color), out)
