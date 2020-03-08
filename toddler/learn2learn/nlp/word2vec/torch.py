import torch
import numpy as np
import torch.functional as F
import torch.nn.functional as F

from torch.autograd import Variable
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
vocabulary_size = len(word_to_id)

W01_dims = (vocabulary_size, embedding_size)
W12_dims = (embedding_size, vocabulary_size)

# Preprocess
training_examples = []

for i in range(window_size, len(corpus) - window_size):
    # Words
    center = corpus[i]
    window = corpus[i-window_size:i] + corpus[i+1:i+window_size+1]

    # Indices
    center_index = word_to_id[center]
    window_indices = [word_to_id[word] for word in window]

    # Training Pair
    training_examples.append((center_index, window_indices))

training_examples = np.array(training_examples)

print('preprocess - done')

# Weights
W01 = Variable(torch.randn(*W01_dims).float(), requires_grad=True)
W12 = Variable(torch.randn(*W12_dims).float(), requires_grad=True)

# Training
for iteration in range(iterations):
    for center_index, window_indices in training_examples:
        layer_0 = center_index
        layer_1 = W01[layer_0]  # Embedding Layer
        layer_2 = torch.matmul(layer_1, W12)
    
        log_softmax = F.log_softmax(layer_2, dim=0)
        loss = F.nll_loss(log_softmax.reshape(1, -1), window_indices)

        loss_val += loss.data[0]
        loss.backward()

        W01.data -= alpha * W01.grad.data
        W12.data -= alpha * W12.grad.data

    if not iteration % 1:
        print(np.square(target_layer - layer_2).sum())
