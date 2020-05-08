from tools.io import sndread_dir, play
from tools.audio import real_spectrogram, real_inv_spectrogram

from tensorflow.keras import backend as K
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from tensorflow.keras.callbacks import TensorBoard

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Parameters
num_freqs = 64
sample_rate = 16000
colors = ['r.', 'g.', 'b.', 'y.', 'k.', 'm.', 'c.']
base_dir = './data/speech/speech_commands_v0.02/{}'

# Read data
word_0 = sndread_dir(base_dir.format('dog'), num_files=5)
word_1 = sndread_dir(base_dir.format('happy'), num_files=5)
word_2 = sndread_dir(base_dir.format('forward'), num_files=5)

# X = np.vstack((word_0, word_1, word_2))

# # Spectrograms
# x_train = tf.stack([
#     np.expand_dims(np.abs(real_spectrogram(word, num_freqs)), axis=-1)
#     for word in X
# ])


# # Convolutions
# input_img = Input(shape=(num_freqs, sample_rate, 1))

# x = Conv2D(16, (3, 3), activation='relu', padding='same')(input_img)
# encoded = MaxPooling2D((2, 2), padding='same')(x)

# x = Conv2D(8, (3, 3), activation='relu', padding='same')(encoded)
# x = UpSampling2D((2, 2))(x)

# decoded = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(x)

# autoencoder = Model(input_img, decoded)
# autoencoder.compile(optimizer='adam', loss='binary_crossentropy')


# autoencoder.fit(x_train, x_train,
#                 epochs=200,
#                 steps_per_epoch=1,
#                 callbacks=[TensorBoard(log_dir='/tmp/autoencoder')])
