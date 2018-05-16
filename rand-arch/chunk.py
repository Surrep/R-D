from sklearn.datasets import fetch_mldata
from math import sin, pi, tan, cos, inf

import matplotlib.pyplot as plt
import numpy as np

mnist = fetch_mldata('MNIST original')


def index_list(data):
    indices = np.indices(data.shape)
    return np.vstack([
        indices[i].ravel() for i in range(len(indices))
    ])


print(index_list(mnist.data[0].reshape(28, 28)))
