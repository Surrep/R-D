from tools.loaders import SpeechCommands
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Utility Functions
def show(title):
    plt.title(title)
    plt.legend()
    plt.show()


def sample(items, size):
    sample_range = range(len(items))

    return [(items[i], i) for i in np.random.choice(sample_range, size, False)]


# Setup
words = SpeechCommands.all_words

rhymes = [('forward', 9), ('backward', 0), ('tree', 28),
          ('sheila', 24), ('three', 27), ('go', 11), ('no', 17)]

colors = ['tab:blue', 'tab:orange', 'tab:green',
          'tab:red', 'tab:purple', 'tab:brown', 'tab:pink']

# Parameters
samples = 4
dim_embed = 2
num_files = 1000
num_classes = len(words)
num_examples = num_classes * num_files
labels = np.arange(num_examples) // num_files


# Training Data
x_raw = SpeechCommands.load_raw(words, num_files)
x_train = tf.expand_dims(SpeechCommands.load_spec(words, num_files), -1)
y_train = tf.keras.utils.to_categorical(labels)

# Model
model = tf.keras.Sequential()

model.add(tf.keras.layers.Input(shape=x_train.shape[1:]))

model.add(tf.keras.layers.Conv2D(32, (3, 3), padding='same'))
model.add(tf.keras.layers.Activation('relu'))

model.add(tf.keras.layers.Conv2D(32, (3, 3)))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(tf.keras.layers.Dropout(0.25))

model.add(tf.keras.layers.Conv2D(64, (3, 3), padding='same'))
model.add(tf.keras.layers.Activation('relu'))

model.add(tf.keras.layers.Conv2D(64, (3, 3)))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(tf.keras.layers.Dropout(0.25))

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(num_classes))
model.add(tf.keras.layers.Activation('softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy')
model.fit(x=x_train, y=y_train, batch_size=100, epochs=8)

# Convolutional LDA Plot
layer_model = tf.keras.Model(inputs=model.input,
                             outputs=model.layers[-2].output)  # dense

predictions = layer_model.predict(x_train).reshape(num_examples, -1)

lda = LDA(n_components=dim_embed)
embeddings = lda.fit_transform(predictions, labels)

for color, (word, i) in zip(colors, rhymes):
    plt.scatter(embeddings[labels == i, 0],
                embeddings[labels == i, 1], c=color, label=word)

show('Convolutional LDA as Applied to Rhyming Words')

# Conventional LDA Plot
raw_clips = np.vstack([x_raw[labels == i] for _, i in rhymes])
raw_labels = np.vstack([labels[labels == i] for _, i in rhymes]).ravel()

lda = LDA(n_components=dim_embed)
raw_embeddings = lda.fit_transform(raw_clips, raw_labels)

for color, (word, i) in zip(colors, rhymes):
    plt.scatter(raw_embeddings[raw_labels == i, 0],
                raw_embeddings[raw_labels == i, 1], c=color, label=word)

show('Conventional LDA as Applied to Rhyming Words')
