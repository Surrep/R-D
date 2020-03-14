from tools.io import sndread
from tools.plot import slide, animate, plot, imshow_many, imshow
from tools.sound import dft, sinusoid, transform, spectrogram

import numpy as np

sample_rate, signal = sndread(
    'data/speech/speech_commands_v0.02/go/0a2b400e_nohash_1.wav')

spec = spectrogram(signal, range(1000))

imshow(np.abs(spec))
