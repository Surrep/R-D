from scipy.io.wavfile import read, write
from sound import Sound
from image import get_colors


import functools
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import glob
import sys
import os

offset = 0
step = 1000
freq_bins = 1000

#####################################################
np.set_printoptions(suppress=True, linewidth=1000, threshold=np.nan)

sound_lib_path = '/Users/tru/Desktop/.../sounds/'
chops_lib_path = '/Users/tru/Desktop/.../chops/'

sounds = [Sound(sound_lib_path + file_name) for file_name in sys.argv[1:]]
s0 = sounds[0].normalize()

for file in glob.glob(chops_lib_path + '*'):
    os.remove(file)

######################################################

class Word():
    def __init__(self):
        self.s = 0
        self.e = 0
        self.frames = []

    def mark(self, i):
        if self.s:
            self.e = i
        else:
            self.s = i
    
    def snap(self, frame):
        self.frames.append(frame)
    
    def in_progress(self):
        return self.s
    
    def get_bounds(self):
        return self.s, self.e
    
    def pronounce(self):
        def tick(a,b):
            res = np.dot(a,b)
            return res / np.max(res)

        return functools.reduce(tick, self.frames).sum()


words = []
word = Word()
for i in range(offset, len(s0.data) - freq_bins, step):
    freqs = s0.get_frequencies(i, i + freq_bins)    
    noise = np.round(np.linalg.norm(freqs),0) > 10

    if word.in_progress():
        if not noise:
            word.mark(i) # marks end

            write(
                chops_lib_path+'{}-{}.wav'.format(*word.get_bounds()),
                44100, 
                s0.data[slice(*word.get_bounds())]
            )

            words.append(word)
            word = Word()
        else:
            word.snap(freqs) 

    elif noise:
        word.mark(i) # marks start
        word.snap(freqs) 
    
    
    

        
pronunciations = [word.pronounce() for word in words]

