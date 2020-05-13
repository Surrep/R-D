from tools.loaders import SpeechCommands
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

import numpy as np
import matplotlib.pyplot as plt

# Setup
colors = ['r', 'g', 'b', 'y']
words = ['backward', 'bird', 'marvin', 'happy']

# Parameters
num_files = 100
num_words = len(words)
num_examples = num_words * num_files
labels = np.arange(num_examples) // num_files

# Load Raw
raw_samples = SpeechCommands.load_raw(words=words,
                                      num_files=num_files,
                                      as_tf=False)

# PCA
lda = LDA(n_components=2)
components = lda.fit_transform(raw_samples, labels)

# Plot
for i, (color, word) in enumerate(zip(colors, words)):
    s = i * num_files
    e = (i+1) * num_files

    plt.scatter(components[s:e, 0], components[s:e, 1], c=color, label=word)

plt.title('Linear Discriminant Analysis as Applied to Raw Audio')
plt.legend()
plt.show()
