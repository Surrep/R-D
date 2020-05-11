from tools.plot import slide
from tools.io import sndread_dir, play
from tools.audio import real_spectrogram

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


# Setup
base_dir = './data/speech/speech_commands_v0.02/{}'

words = ['learn', 'left', 'marvin', 'nine', 'no', 'off',
         'right', 'seven', 'sheila', 'three', 'tree']

colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
          'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']

# Parameters
num_freqs = 64
sample_rate = 16000
num_files_per_word = 8
num_classes = len(words)
num_examples = num_classes * num_files_per_word

# Read data
raw_audio = np.vstack([
    sndread_dir(base_dir.format(word), num_files_per_word)
    for word in words
])

x_train = tf.stack([
    np.expand_dims(np.abs(real_spectrogram(word_audio, num_freqs)), axis=-1)
    for word_audio in raw_audio
])

labels = np.arange(num_classes * num_files_per_word) // num_files_per_word
y_train = tf.keras.utils.to_categorical(labels)

# Construct model
model = tf.keras.Sequential()

model.add(tf.keras.layers.Input(shape=x_train.shape[1:]))

model.add(tf.keras.layers.Conv2D(32, (3, 3), padding='same'))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(1, 32)))

model.add(tf.keras.layers.Conv2D(16, (3, 3), padding='same'))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(4, 32)))

model.add(tf.keras.layers.Conv2D(4, (1, 1), padding='same'))
model.add(tf.keras.layers.Activation('relu'))

model.add(tf.keras.layers.Conv2D(1, (1, 1), padding='same'))
model.add(tf.keras.layers.Activation('relu'))

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(num_classes))
model.add(tf.keras.layers.Activation('softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy')
model.fit(x=x_train, y=y_train, batch_size=num_files_per_word, epochs=200)

# Embeddings
layer_name = 'dense_5'
intermediate_layer = tf.keras.Model(inputs=model.input,
                                    outputs=model.get_layer(layer_name).output)
predictions = intermediate_layer.predict(x_train).reshape(num_examples, -1)

lda = LDA(n_components=2)
embeddings = lda.fit_transform(predictions, labels)

# Plot
for i, (color, word) in enumerate(zip(colors, words)):
    plt.scatter(embeddings[labels == i, 0],
                embeddings[labels == i, 1], c=color, label=word)

plt.legend()
plt.show()
