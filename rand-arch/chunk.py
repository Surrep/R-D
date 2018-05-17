from sklearn.datasets import fetch_mldata
from math import sin, pi, tan, cos, inf

import matplotlib.pyplot as plt
import numpy as np

mnist = fetch_mldata('MNIST original')


def index_list(data):
    indices = np.indices(data.shape)
    return np.vstack([
        indices[i].ravel() for i in range(len(indices))
    ]).T


def rand_rect(max_area):
    w = np.random.randint(max_area) + 1
    h = int(max_area / w)

    return (w, h)


def init_weights(data_chunks, dims):
    return [
        np.random.randn(chunk.shape[0], dims) * 0.1
        for chunk in data_chunks
    ]


def forward(data_chunks, weights):
    return [chunk.T.dot(W).sum() for (chunk, W) in zip(data_chunks, weights)]


def chunk_input(data):
    indices = index_list(data)
    r_indxs = list(np.random.choice(
        len(indices), size=len(indices), replace=False))

    chunks = []
    while r_indxs:
        area = np.random.randint(len(r_indxs) / 64)
        w, h = rand_rect(area + 1)

        chunk = np.array([data[tuple(indices[r_indxs.pop()])]
                          for _ in range(w * h)])

        chunks.append(chunk.reshape(w, h))

    return chunks


a = mnist.data[0]

input_chunks = chunk_input(a.reshape(28, 28))
weights = init_weights(input_chunks, dims=3)
out = forward(input_chunks, weights)


