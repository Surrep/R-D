from scipy.io.wavfile import read, write
from scipy.misc import imread, imsave
from IPython.display import Audio
from image import get_colors

from matplotlib.widgets import Slider
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import sys

rate, data = read('/Users/tru/Desktop/.../sounds/' + sys.argv[1])
data = data[:,1] / np.max(data)

s = 100000
e = 150000
r = 1000

fig, ax = plt.subplots()
l, = plt.plot(0,0,'.')
plt.axis([-40,40,-40,40])
t = ax.text(7,7,'')



axamp = plt.axes([0.25, .03, 0.50, 0.02])
samp = Slider(axamp, 'Amp', 0, e-s, valinit=0)

def update(val):
    v = int(val)
    new_data = np.fft.fft(data[s+v:s+v+r])
    t.set_text(np.linalg.norm(new_data))
    l.set_data(new_data.real, new_data.imag)
    fig.canvas.draw_idle()

samp.on_changed(update)

plt.show()