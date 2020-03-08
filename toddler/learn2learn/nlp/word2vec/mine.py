import numpy as np
from ...utilities.io import load_corpus, make_vocab

# Load Data
path = "/Users/trumanpurnell/Workspace/bb-labs/far/data/bible.txt"
corpus = load_corpus(path)
word_to_id, id_to_word = make_vocab(corpus)
print('loading - done')

# Hyperparameters
alpha = 0.01
iterations = int(4e2)
window_size = 6
embedding_size = 200

weights_0_1_dims = (len(word_to_id), embedding_size)
weights_1_2_dims = (embedding_size, len(word_to_id))

# Preprocess
X_train = []
Y_train = []

for i in range(window_size, len(corpus) - window_size):
    # Words
    center = corpus[i]
    window = corpus[i-window_size:i] + corpus[i+1:i+window_size+1]

    # Indices
    center_index = word_to_id[center]
    window_indices = [word_to_id[word] for word in window]

    # Training Pair
    X_train.append(center_index)
    Y_train.append(window_indices)

training_examples = np.array([X_train, Y_train])

print('preprocess - done')

# Weights
weights_0_1 = np.random.randn(*weights_0_1_dims) / 100
weights_1_2 = np.random.randn(*weights_1_2_dims) / 100

# Training
for iteration in range(iterations):
    for ti in range(0, len(X_train)):
        center_index = X_train[ti]
        window_indices = Y_train[ti]

        layer_0 = center_index
        layer_1 = weights_0_1[layer_0].reshape(1, -1)  # Embedding Layer
        layer_2 = layer_1.dot(weights_1_2)

        target_layer = np.zeros(len(word_to_id)).reshape(1, -1)
        target_layer[:, window_indices] = 3

        layer_2_delta = layer_2 - target_layer
        layer_1_delta = layer_2_delta.dot(weights_1_2.T)

        weights_1_2_grad = layer_1.T.dot(layer_2_delta)
        weights_0_1_grad = layer_1_delta

        weights_1_2 -= alpha * weights_1_2_grad
        weights_0_1[layer_0] -= alpha * weights_0_1_grad.reshape(-1)

    if not iteration % 1:
        print(np.square(target_layer - layer_2).sum())


def most_similiar(input_word='god', k=10):
    input_vector = weights_0_1[word_to_id[input_word]]
    distances = np.linalg.norm(weights_0_1 - input_vector, axis=1)
    sorted_ids = np.argsort(distances)

    return zip([id_to_word[word_id] for word_id in sorted_ids[1:k]], distances[sorted_ids[1:k]])
