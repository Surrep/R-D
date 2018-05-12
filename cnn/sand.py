from sklearn.datasets import fetch_mldata
import matplotlib.pyplot as plt
import numpy as np

mnist = fetch_mldata('MNIST original')
i0 = mnist.data[0].reshape(28, 28)
i1 = mnist.data[1].reshape(28, 28)

W1 = np.random.randn(28, 2)
W2 = np.random.randn(28, 1)


def forward(image):
    return image.dot(W1).T.dot(W2)


print(forward(i0))
print(forward(i1))
