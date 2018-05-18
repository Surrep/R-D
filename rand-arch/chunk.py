from sklearn.datasets import fetch_mldata
from random_net import RandomNeuralNetwork

import matplotlib.pyplot as plt
import numpy as np

mnist = fetch_mldata('MNIST original')
a = mnist.data[0].reshape(28, 28)

rnn = RandomNeuralNetwork(X=a)
