import numpy as np


def relu(z):
    return np.maximum(0, z)


def tanh(z):
    return np.tanh(z)
