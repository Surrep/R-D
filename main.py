from tools.plot import slide
from tools.io import sndread_dir, play
from tools.audio import real_spectrogram, real_inv_spectrogram

import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_freqs = 1000
sample_rate = 16000
colors = ['r.', 'g.', 'b.', 'y.', 'k.', 'm.', 'c.']

# Read data
X = sndread_dir('./data/speech/speech_commands_v0.02/happy')

# Spectrogram
spectrogram = real_spectrogram(signal=X[1], num_freqs=num_freqs)

# Display
plt.imshow(np.abs(spectrogram), aspect='auto')
plt.show()
