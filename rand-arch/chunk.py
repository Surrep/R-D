from sklearn.datasets import fetch_mldata
from meta import MetaNet

import matplotlib.pyplot as plt
import numpy as np

mnist = fetch_mldata('MNIST original')
a = mnist.data[0].reshape(28, 28)

mn = MetaNet(X_shape=(5, 5))

[print(synapse.shape) for synapse in mn.network]
