from tools.loaders import SpeechCommands
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt

# Setup
colors = ['r', 'g', 'b', 'y']
words = ['yes', 'up', 'right', 'follow']

# Parameters
num_files = 100

# Load Raw
raw_samples = SpeechCommands.load_raw(words=words,
                                      num_files=num_files,
                                      as_tf=False)

# PCA
pca = PCA(n_components=2)
components = pca.fit_transform(raw_samples)

# Plot
for i, (color, word) in enumerate(zip(colors, words)):
    s = i * num_files
    e = (i+1) * num_files

    plt.scatter(components[s:e, 0], components[s:e, 1], c=color, label=word)

plt.title('Principle Component Analysis as Applied to Raw Audio')
plt.legend()
plt.show()

