from scipy.io.wavfile import read, write
from sound import Sound
from image import get_colors

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import glob
import sys
import os

np.set_printoptions(suppress=True, linewidth=1000, threshold=np.nan)

sound_lib_path = '/Users/tru/Desktop/.../sounds/'
chops_lib_path = '/Users/tru/Desktop/.../chops/'

sounds = [Sound(sound_lib_path + file_name) for file_name in sys.argv[1:]]
s0 = sounds[0]

for file in glob.glob(chops_lib_path + '*'):
    os.remove(file)


offset = 0
step = 1000
freq_bins = 1000


word = [0,0]
for i in range(offset, len(s0.data) - freq_bins, step):
    freqs = s0.get_frequencies(i, i + freq_bins)    
    bump = np.round(np.linalg.norm(freqs) / 1.2e11,0)

    if bump and not word[0]:
        word[0] = i
        continue
    
    if not bump and word[0]:
        word[1] = i
        write(chops_lib_path+'{}-{}.wav'.format(*word),44100, s0.data[slice(*word)])
        word = [0,0]
        continue
    