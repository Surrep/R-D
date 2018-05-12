from sklearn.datasets import fetch_mldata
import matplotlib.pyplot as plt

mnist = fetch_mldata('MNIST original')
plt.imshow(mnist.data[1].reshape(28, 28))
plt.show()
