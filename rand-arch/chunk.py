from sklearn.datasets import fetch_mldata
from math import sin, pi, tan, cos, inf

import matplotlib.pyplot as plt
import numpy as np

mnist = fetch_mldata('MNIST original')
dims = 2


def get_indices(data):
    indices = np.indices(data.shape)
    return np.vstack([
        indices[i].ravel() for i in range(len(indices))
    ]).T


def random_layer(neurons):
    w = np.random.randint(max_area) + 1
    h = int(max_area / w)

    return (w, h)


def generate_architecture(input_data, output_dim):
    valid_indices = get_indices(input_data)
    i_count = len(valid_indices)
    rand_inds = list(np.random.choice(i_count, size=i_count, replace=False))

    while rand_inds:  # while there is data left to group
        neuron_count = np.random.randint(len(rand_inds))
        layer = random_layer(size=neuron_count, depth=len(input_data.shape))

        chunk = np.array([data[tuple(indices[r_indxs.pop()])]
                          for _ in range(w * h)])

        chunks.append(chunk.reshape(w, h))


def init_weights(data_chunks, dims):
    return [
        np.random.randn(chunk.shape[0], dims) * 0.1
        for chunk in data_chunks
    ]


def forward(data_chunks, weights):
    return np.array([chunk.T.dot(W).sum() for (chunk, W) in zip(data_chunks, weights)])


a = mnist.data[0]

input_chunks = chunk_input(a.reshape(28, 28))
weights = init_weights(input_chunks, dims=dims)
out = forward(input_chunks, weights)

final_layer = np.random.randn(len(out), dims)
points = out.reshape(1, -1).dot(final_layer)

plt.scatter(points[:, 0], points[:, 1], c=targets)
plt.show()
