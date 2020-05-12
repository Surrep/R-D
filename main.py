from tools.loaders import SpeechCommands
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Setup
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
          'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']

words = ['backward', 'bird', 'marvin', 'happy']

# Parameters
sample_rate = 16000
num_freqs = 64
num_files = 20
num_classes = len(words)
num_examples = num_classes * num_files
labels = np.arange(num_examples) // num_files

# Read data
x_train = SpeechCommands.load_spec(words)
y_train = tf.keras.utils.to_categorical(labels)

# Construct model
model = tf.keras.Sequential()

model.add(tf.keras.layers.Input(shape=x_train.shape[1:]))

model.add(tf.keras.layers.Conv2D(4, (3, 3), padding='same'))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(1, 32)))

model.add(tf.keras.layers.Conv2D(4, (3, 3), padding='same'))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(4, 32)))

model.add(tf.keras.layers.Conv2D(4, (1, 1), padding='same'))
model.add(tf.keras.layers.Activation('relu'))

model.add(tf.keras.layers.Conv2D(4, (1, 1), padding='same'))
model.add(tf.keras.layers.Activation('relu'))

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(num_classes))
model.add(tf.keras.layers.Activation('softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy')
model.fit(x=x_train, y=y_train, batch_size=20, epochs=100)

# Embeddings
dense = tf.keras.Model(inputs=model.input, outputs=model.layers[-2].output)
predictions = dense.predict(x_train).reshape(num_examples, -1)

lda = LDA(n_components=2)
embeddings = lda.fit_transform(predictions, labels)

# Plot
for i, (color, word) in enumerate(zip(colors, words)):
    plt.scatter(embeddings[labels == i, 0],
                embeddings[labels == i, 1], c=color, label=word)

plt.legend()
plt.show()
