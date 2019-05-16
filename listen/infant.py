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

step = 150
freq_bins = 550

sounds = [Sound(path=sound_lib_path + file_name, freq_bins=freq_bins).normalize() for file_name in sys.argv[1:]]

for file in glob.glob(chops_lib_path + '*'):
    os.remove(file)

########################################################

bumps = []

for si,sound in enumerate(sounds):
    for i in range(450000, 560000, step):
        freqs = sound.get_frequencies(i, i + freq_bins)    
        print(freqs[2], freqs[-2])
        print(freqs[2] * freqs[-2])
        noise = freqs[:freq_bins//2] * freqs[freq_bins//2:]
        print(noise[2])
        break
        
        

        
        # if sound.is_within_word() and not sound.makes_trivial_word(i) and not noise:
        #     word = sound.end_word(i)

        #     write(
        #         chops_lib_path+'{}-{}-{}'.format(*word,sys.argv[1:][si]),
        #         44100, 
        #         sound.data[slice(*word)]
        #     ) 

        # elif not sound.is_within_word() and noise:
        #     sound.start_word(i)

plt.plot(bumps)
plt.show()

# for sii,sound in enumerate(sounds):
#     print('------------',sys.argv[1:][si],'------------')
#     for wi,word in enumerate(sound.words):
#         print(word, wi)


# def get_top_specs(snd, top=35):
#     top_specs = np.zeros((24000,10)).astype(np.int64)

#     for i,spectra in enumerate(snd.get_spectrogram()):
#         top_specs[i] = np.argsort(np.absolute(spectra))[:10]
        
#     return np.argsort(np.bincount(top_specs.reshape(-1)))[:top]


# print(get_top_specs(sounds[0]))
# print(get_top_specs(sounds[1]))

# w0 = sounds[0].get_spectrogram()
# w1 = sounds[1].get_spectrogram()

# fig, axes = plt.subplots(1, 1)

# def animate(i):
#     plt.plot(w0[i].real[:], w0[i].imag[:], 'bo')
#     plt.plot(w1[i].real[:], w1[i].imag[:], 'rs')


# ani = animation.FuncAnimation(fig, animate, frames=120000, interval=2000)
# plt.show()
