import numpy as np

from keras.datasets import mnist
from ...utilities.plotting import show_image_grid


# Get training data:
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalize images
test_images = X_test.reshape(-1, 784) / 255
train_images = X_train.reshape(-1, 784) / 255

# One-hot encode labels
y_train_hot = np.zeros((y_train.size, 10))
y_train_hot[np.arange(y_train.size), y_train] = 100

y_test_hot = np.zeros((y_test.size, 10))
y_test_hot[np.arange(y_test.size), y_test] = 1

# Assign one-hot labels
test_labels = y_test_hot
train_labels = y_train_hot

# Initialize the Weights: 10 Template Images which we will match against
weights = 0.2 * np.random.random((784, 10)) - 0.1

# Train
alpha = 0.0000008
for i in range(500):
    predictions = train_images.dot(weights)
    deltas = predictions - train_labels
    error = np.linalg.norm(deltas)
    gradient = train_images.T.dot(deltas)

    weights -= alpha * gradient

    if not (i % 10):
        print(error)

# Test
predictions = test_images.dot(weights)
accuracy = np.argmax(predictions, axis=1) == y_test

print(np.sum(accuracy) / np.size(accuracy))

# Misses
all_miss_indices = np.argwhere(accuracy == False).flatten()
sample_miss_indices = np.random.choice(all_miss_indices, size=100)
sample_miss_images = test_images[sample_miss_indices]

show_image_grid(weights.T.reshape(-1, 28, 28), 2, 5)
