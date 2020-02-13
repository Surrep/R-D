import string
import numpy as np

with open("./data/bible.txt") as fs:
    without_punctuation = str.maketrans('', '', string.punctuation)

    corpus = fs.read().lower().translate(without_punctuation).split()
    vocab = {k: v for v, k in enumerate(corpus)}

# Hyperparameters
alpha = 0.0001
iterations = int(1e0)
window_size = 3
embedding_size = 40

weights_0_1_dims = (len(vocab), embedding_size)
weights_1_0_dims = (embedding_size, len(vocab))

# Weights
weights_0_1 = np.random.randn(*weights_0_1_dims)
weights_1_0 = np.random.randn(*weights_1_0_dims)

# Training
sample = corpus[:16]

for iteration in range(iterations):
    for si in range(window_size, len(sample) - window_size + 1):
        window = sample[si-window_size: si+window_size]
        
