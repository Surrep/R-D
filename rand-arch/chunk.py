from sklearn.datasets import fetch_mldata
from math import sin, pi, tan, cos, inf, pow

import matplotlib.pyplot as plt
import numpy as np

mnist = fetch_mldata('MNIST original')


def get_indices(shape):
    index_grid = np.indices(shape)
    indices = np.vstack([
        index_grid[i].ravel() for i in range(len(index_grid))
    ]).T

    return (indices, len(indices))


def random_layer(size, depth):
    return tuple([
        np.random.randint(pow(size, 1 / depth)) + 1
        for _ in range(depth)
    ])


def generate_architecture(in_shape, out_shape):
    indices = np.prod(in_shape)

    layers = []
    while indices:  # while there is data left to group
        neuron_count = np.random.randint(indices) + 1
        layer = random_layer(size=neuron_count, depth=len(in_shape))
        layers.append(layer)

        indices -= np.prod(layer)

    return layers


def feed(arch, data):
    pass


a = mnist.data[0].reshape(28, 28)
arch = generate_architecture(in_shape=a.shape, out_shape=None)
print(arch)
