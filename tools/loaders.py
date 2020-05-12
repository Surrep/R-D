from .io import specread_dir, sndread_dir

import numpy as np
import tensorflow as tf


class Bible():

    @classmethod
    def load_corpus(path):
        with open(path) as fs:
            no_punctuation = str.maketrans('', '', string.punctuation)
            corpus = fs.read().lower().translate(no_punctuation).split()

        return corpus

    @classmethod
    def make_vocab(corpus):
        word_to_id = {}
        id_to_word = {}

        identity = 0

        for word in corpus:
            if word not in word_to_id:
                word_to_id[word] = identity
                id_to_word[identity] = word
                identity += 1

        return word_to_id, id_to_word


class SpeechCommands():
    base_dir_raw = './data/audio/speech_commands/raw/{}'
    base_dir_spec = './data/audio/speech_commands/spec/{}'

    all_words = ['backward', 'bed', 'bird', 'cat', 'dog',
                 'down', 'eight', 'five', 'follow', 'forward',
                 'four', 'go', 'happy', 'house', 'learn', 'left',
                 'nine', 'no', 'off', 'on', 'one', 'right', 'marvin',
                 'seven', 'sheila', 'six', 'stop', 'three', 'tree',
                 'two', 'up',  'visual', 'wow', 'yes', 'zero']

    @classmethod
    def load(context, words, num_files, base_dir, load_method, as_tf=True):
        if words is None:
            words = context.all_words

        result = np.vstack([
            load_method(base_dir.format(word), num_files)
            for word in words
        ])

        return result if not as_tf else tf.convert_to_tensor(result)

    @classmethod
    def load_raw(context, words=None, num_files=None, as_tf=True):
        return context.load(words,
                            num_files,
                            context.base_dir_raw,
                            sndread_dir,
                            as_tf)

    @classmethod
    def load_spec(context, words=None, num_files=None, as_tf=False):
        return context.load(words,
                            num_files,
                            context.base_dir_spec,
                            specread_dir,
                            as_tf)
