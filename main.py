from tools.io import sndread_dir, play
from tools.audio import real_spectrogram, real_inv_spectrogram

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Misc
num_freqs = 64
sample_rate = 16000
num_files_per_word = 1
colors = ['r.', 'g.', 'b.', 'y.', 'k.', 'm.', 'c.']
base_dir = './data/speech/speech_commands_v0.02/{}'
words = ['dog', 'happy', 'forward', 'sheila', 'six', 'right', 'up']

# Read data
x_train = tf.stack([
    np.expand_dims(np.abs(real_spectrogram(word_audio, num_freqs)), axis=-1)
    for word_audio in np.vstack([
        sndread_dir(base_dir.format(word), num_files_per_word)
        for word in words
    ])
])


# Convolutions
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(num_freqs, sample_rate, 1)),
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D((2, 2), padding='same'),
    tf.keras.layers.Conv2D(8, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.UpSampling2D((2, 2)),
    tf.keras.layers.Conv2D(1, (3, 3), activation='sigmoid', padding='same'),
])

model.compile(optimizer='adam', loss='binary_crossentropy')

model.fit(x=x_train,
          y=x_train,
          epochs=10,
          steps_per_epoch=1,
          callbacks=[
              tf.keras.callbacks.TensorBoard(log_dir='/tmp/autoencoder')
          ])
