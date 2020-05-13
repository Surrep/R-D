from .io import specread_dir, sndread_dir
from .audio import real_spectrogram

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
    sample_rate = 16000
    base_dir_raw = './data/audio/speech_commands/raw/{}'
    base_dir_spec = './data/audio/speech_commands/spec/{}'

    all_words = ['backward', 'bed', 'bird', 'cat', 'dog',
                 'down', 'eight', 'five', 'follow', 'forward',
                 'four', 'go', 'happy', 'house', 'learn', 'left',
                 'nine', 'no', 'off', 'on', 'one', 'right', 'marvin',
                 'seven', 'sheila', 'six', 'stop', 'three', 'tree',
                 'two', 'up',  'visual', 'wow', 'yes', 'zero']

    all_counts = [1664, 2014, 2064, 2031, 2128, 3917, 3787, 4052, 1579, 1557,
                  3728, 3880, 2054, 2113, 1575, 3801, 3934, 3941, 3745, 3845,
                  3890, 3778, 2100, 3998, 2022, 3860, 3872, 3727, 1759, 3880,
                  3723, 1592, 2123, 4044, 4052]

    # TODO #
    @classmethod
    def write_specs(context, words, num_files, num_freqs):
        pass
        # skip = context.sample_rate // num_freqs

        # raw_audio = SpeechCommands.load_raw(num_files=num_files)

        # for i, word in enumerate(SpeechCommands.all_words):
        #     s = i * num_files
        #     e = (i+1) * num_files
        #     base_dir = SpeechCommands.base_dir_spec.format(word)

        #     for j, sample in enumerate(raw_audio[s:e]):
        #         path = '{}/{}'.format(base_dir, j)
        #         np.save(file=path,
        #              arr=np.abs(real_spectrogram(sample, num_freqs, skip)))

    @classmethod
    def load(context, words, num_files, base_dir, load_method, as_tf=True):
        if not words:
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
