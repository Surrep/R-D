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
step = 750
freq_bins = 750

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

    def mark(self, i):
        if self.s:
            self.e = i
        else:
            self.s = i
    
    def in_progress(self):
        return self.s
    
    def get_bounds(self):
        return self.s, self.e
    
    def pronounce(self):
        return functools.reduce(lambda a,b: a-b, self.frames)
    
    def gather_freqs(self):
        self.frames = [s0.get_frequencies(i,i+freq_bins) for i in range(self.s,self.e)]


words = []
word = Word()
for i in range(offset, len(s0.data) - freq_bins, step):
    freqs = s0.get_frequencies(i, i + freq_bins)    
    noise = np.round(np.linalg.norm(freqs),0)

    if word.in_progress() and not noise:
        word.mark(i) # marks end

        write(
            chops_lib_path+'{}-{}.wav'.format(*word.get_bounds()),
            44100, 
            s0.data[slice(*word.get_bounds())]
        )

        words.append(word)
        word = Word()    

    elif noise:
        word.mark(i) # marks start
    

words[5].gather_freqs()
for frame in words[5].frames:
    frame[np.absolute(frame) < 0.4] = 0

plt.plot(words[5].frames[0].real,words[5].frames[0].imag,'bo')
plt.plot(words[5].frames[1].real,words[5].frames[1].imag,'r^')
plt.plot(words[5].frames[2].real,words[5].frames[2].imag,'g*')
plt.plot(words[5].frames[3].real,words[5].frames[3].imag,'md')
plt.plot(words[5].frames[4].real,words[5].frames[4].imag,'y<')
plt.plot(words[5].frames[5].real,words[5].frames[5].imag,'k>')
plt.plot(words[5].frames[6].real,words[5].frames[6].imag,'cs')

plt.plot(words[5].frames[0+7].real,words[5].frames[0+7].imag,'bo')
plt.plot(words[5].frames[1+7].real,words[5].frames[1+7].imag,'r^')
plt.plot(words[5].frames[2+7].real,words[5].frames[2+7].imag,'g*')
plt.plot(words[5].frames[3+7].real,words[5].frames[3+7].imag,'md')
plt.plot(words[5].frames[4+7].real,words[5].frames[4+7].imag,'y<')
plt.plot(words[5].frames[5+7].real,words[5].frames[5+7].imag,'k>')
plt.plot(words[5].frames[6+7].real,words[5].frames[6+7].imag,'cs')

plt.plot(words[5].frames[0 + 14].real,words[5].frames[0 + 14].imag,'bo')
plt.plot(words[5].frames[1 + 14].real,words[5].frames[1 + 14].imag,'r^')
plt.plot(words[5].frames[2 + 14].real,words[5].frames[2 + 14].imag,'g*')
plt.plot(words[5].frames[3 + 14].real,words[5].frames[3 + 14].imag,'md')
plt.plot(words[5].frames[4 + 14].real,words[5].frames[4 + 14].imag,'y<')
plt.plot(words[5].frames[5 + 14].real,words[5].frames[5 + 14].imag,'k>')
plt.plot(words[5].frames[6 + 14].real,words[5].frames[6 + 14].imag,'cs')

plt.plot(words[5].frames[0+21].real,words[5].frames[0+21].imag,'bo')
plt.plot(words[5].frames[1+21].real,words[5].frames[1+21].imag,'r^')
plt.plot(words[5].frames[2+21].real,words[5].frames[2+21].imag,'g*')
plt.plot(words[5].frames[3+21].real,words[5].frames[3+21].imag,'md')
plt.plot(words[5].frames[4+21].real,words[5].frames[4+21].imag,'y<')
plt.plot(words[5].frames[5+21].real,words[5].frames[5+21].imag,'k>')
plt.plot(words[5].frames[6+21].real,words[5].frames[6+21].imag,'cs')

plt.plot(words[5].frames[0+28].real,words[5].frames[0+28].imag,'bo')
plt.plot(words[5].frames[1+28].real,words[5].frames[1+28].imag,'r^')
plt.plot(words[5].frames[2+28].real,words[5].frames[2+28].imag,'g*')
plt.plot(words[5].frames[3+28].real,words[5].frames[3+28].imag,'md')
plt.plot(words[5].frames[4+28].real,words[5].frames[4+28].imag,'y<')
plt.plot(words[5].frames[5+28].real,words[5].frames[5+28].imag,'k>')
plt.plot(words[5].frames[6+28].real,words[5].frames[6+28].imag,'cs')

plt.plot(words[5].frames[0+35].real,words[5].frames[0+35].imag,'bo')
plt.plot(words[5].frames[1+35].real,words[5].frames[1+35].imag,'r^')
plt.plot(words[5].frames[2+35].real,words[5].frames[2+35].imag,'g*')
plt.plot(words[5].frames[3+35].real,words[5].frames[3+35].imag,'md')
plt.plot(words[5].frames[4+35].real,words[5].frames[4+35].imag,'y<')
plt.plot(words[5].frames[5+35].real,words[5].frames[5+35].imag,'k>')
plt.plot(words[5].frames[6+35].real,words[5].frames[6+35].imag,'cs')

plt.plot(words[5].frames[0+42].real,words[5].frames[0+42].imag,'bo')
plt.plot(words[5].frames[1+42].real,words[5].frames[1+42].imag,'r^')
plt.plot(words[5].frames[2+42].real,words[5].frames[2+42].imag,'g*')
plt.plot(words[5].frames[3+42].real,words[5].frames[3+42].imag,'md')
plt.plot(words[5].frames[4+42].real,words[5].frames[4+42].imag,'y<')
plt.plot(words[5].frames[5+42].real,words[5].frames[5+42].imag,'k>')
plt.plot(words[5].frames[6+42].real,words[5].frames[6+42].imag,'cs')

plt.plot(words[5].frames[0+49].real,words[5].frames[0+49].imag,'bo')
plt.plot(words[5].frames[1+49].real,words[5].frames[1+49].imag,'r^')
plt.plot(words[5].frames[2+49].real,words[5].frames[2+49].imag,'g*')
plt.plot(words[5].frames[3+49].real,words[5].frames[3+49].imag,'md')
plt.plot(words[5].frames[4+49].real,words[5].frames[4+49].imag,'y<')
plt.plot(words[5].frames[5+49].real,words[5].frames[5+49].imag,'k>')
plt.plot(words[5].frames[6+49].real,words[5].frames[6+49].imag,'cs')

plt.plot(words[5].frames[0+56].real,words[5].frames[0+56].imag,'bo')
plt.plot(words[5].frames[1+56].real,words[5].frames[1+56].imag,'r^')
plt.plot(words[5].frames[2+56].real,words[5].frames[2+56].imag,'g*')
plt.plot(words[5].frames[3+56].real,words[5].frames[3+56].imag,'md')
plt.plot(words[5].frames[4+56].real,words[5].frames[4+56].imag,'y<')
plt.plot(words[5].frames[5+56].real,words[5].frames[5+56].imag,'k>')
plt.plot(words[5].frames[6+56].real,words[5].frames[6+56].imag,'cs')

plt.show()