import numpy as np


def squared_error(yhat, y):
    return np.square(yhat - y).sum() / 2


def softmax(yhat, y):
    pass
