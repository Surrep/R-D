import numpy as np
from ..utilities.io import load_corpus, make_vocab

# Load Data
# corpus = load_corpus(
#     "/Users/trumanpurnell/Workspace/bb-labs/far/data/bible.txt")

corpus = ['the', 'quick', 'brown', 'fox',
          'jumped', 'over', 'the', 'lazy', 'dog']

vocab = make_vocab(corpus)

# Hyperparameters
alpha = 0.001
iterations = int(1e5)
window_size = 2
embedding_size = 10

weights_0_1_dims = (len(vocab), embedding_size)
weights_1_2_dims = (embedding_size, len(vocab))

# Preprocess
X_train = []
Y_train = []

for i in range(window_size, len(corpus) - window_size):
    # Words
    center = corpus[i]
    window = corpus[i-window_size:i] + corpus[i+1:i+window_size+1]

    # Indices
    center_index = vocab[center]
    window_indices = [vocab[word] for word in window]

    # Training Pair
    X_train.append(center_index)
    Y_train.append(window_indices)


# Weights
weights_0_1 = np.random.randn(*weights_0_1_dims) / 100
weights_1_2 = np.random.randn(*weights_1_2_dims) / 100

# Training
for iteration in range(iterations):
    for (center_index, window_indices) in zip(X_train, Y_train):
        layer_0 = center_index
        layer_1 = weights_0_1[layer_0].reshape(1, -1)  # Embedding Layer
        layer_2 = layer_1.dot(weights_1_2)

        target_layer = np.zeros(len(vocab)).reshape(1, -1)
        target_layer[:, window_indices] = 3

        layer_2_delta = layer_2 - target_layer
        layer_1_delta = layer_2_delta.dot(weights_1_2.T)

        weights_1_2_grad = layer_1.T.dot(layer_2_delta)
        weights_0_1_grad = layer_1_delta

        weights_1_2 -= alpha * weights_1_2_grad
        weights_0_1[layer_0] -= alpha * weights_0_1_grad.reshape(-1)

    if not iteration % 100:
        print(np.square(target_layer - layer_2).sum())
