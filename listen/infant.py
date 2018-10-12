from scipy.io.wavfile import read, write
from sound import Sound

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import glob
import sys
import os

###################### SETUP #########################
np.set_printoptions(suppress=True, linewidth=1000, threshold=np.nan)

sound_lib_path = '/Users/tru/Desktop/.../sounds/'
chops_lib_path = '/Users/tru/Desktop/.../chops/'

step = 750
freq_bins = 750

sounds = [Sound(sound_lib_path + file_name).normalize() for file_name in sys.argv[1:]]

for file in glob.glob(chops_lib_path + '*'):
    os.remove(file)

########################################################

for si,sound in enumerate(sounds):
    for i in range(0, len(sound.data) - freq_bins, step):
        freqs = sound.get_frequencies(i, i + freq_bins)    
        noise = np.round(np.linalg.norm(freqs), 0)

        if sound.is_within_word() and not noise:
            word = sound.end_word(i)

            write(
                chops_lib_path+'{}-{}-{}'.format(*word,sys.argv[1:][si]),
                44100, 
                sound.data[slice(*word)]
            ) 

        elif not sound.is_within_word() and noise:
            sound.start_word(i)

""" 
7,0
"""    

w0 = sounds[0].get_spectrogram(word=0)
w1 = sounds[1].get_spectrogram(word=7)

fig, axes = plt.subplots(1, 1)

def animate(i):
    plt.plot(w0[i].real[7:9], w0[i].imag[7:9], 'bo')
    plt.plot(w1[i].real[7:9], w1[i].imag[7:9], 'rs')


ani = animation.FuncAnimation(fig, animate, frames=120000, interval=300)
plt.show()