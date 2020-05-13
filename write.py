from tools.audio import real_spectrogram
from tools.loaders import SpeechCommands

import numpy as np

# Parameters
num_files = 1000
num_freqs = 64
sample_rate = 16000
skip = sample_rate // num_freqs

# Setup
raw_audio = SpeechCommands.load_raw(num_files=num_files)

for i, word in enumerate(SpeechCommands.all_words):
    s = i * num_files
    e = (i+1) * num_files
    base_dir = SpeechCommands.base_dir_spec.format(word)

    for j, sample in enumerate(raw_audio[s:e]):
        path = '{}/{}'.format(base_dir, j)
        np.save(file=path,
                arr=np.abs(real_spectrogram(sample, num_freqs, skip)))
