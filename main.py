from tools.io import sndread_dir, play
from tools.audio import real_spectrogram, real_inv_spectrogram

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Setup
words = ['dog', 'cat', 'right', 'visual', 'yes', 'wow', 'up']
colors = ['r.', 'g.', 'b.', 'y.', 'k.', 'm.', 'c.']
base_dir = './data/speech/speech_commands_v0.02/{}'

# Parameters
num_freqs = 64
sample_rate = 16000
num_files_per_word = 5
num_classes = len(words)

# Read data
x_train = tf.stack([
    np.expand_dims(a=np.abs(real_spectrogram(word_audio, num_freqs, skip=4)),
                   axis=-1)
    for word_audio in np.vstack([
        sndread_dir(base_dir.format(word), num_files_per_word)
        for word in words
    ])
])

y_train = tf.keras.utils.to_categorical(
    np.arange(num_classes * num_files_per_word) // num_files_per_word)

# Construct model
model = tf.keras.Sequential()

# Input
model.add(tf.keras.layers.Input(shape=x_train.shape[1:]))

# Conv 1
model.add(tf.keras.layers.Conv2D(8, (3, 3), padding='same'))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(1, 4)))

# Conv 2
model.add(tf.keras.layers.Conv2D(8, (3, 3), padding='same'))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(1, 4)))

# Conv 3
model.add(tf.keras.layers.Conv2D(8, (3, 3), padding='same'))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(1, 4)))

# Conv 4
model.add(tf.keras.layers.Conv2D(8, (3, 3), padding='same'))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(1, 4)))

# Flat
model.add(tf.keras.layers.Flatten())

# Dense
model.add(tf.keras.layers.Dense(num_classes))

# Activations
model.add(tf.keras.layers.Activation('softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy')
model.fit(x=x_train, y=y_train, batch_size=num_files_per_word, epochs=50)
