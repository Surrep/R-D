from sound import Sound

from matplotlib.widgets import Slider
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import sys

s0 = Sound('/Users/tru/Desktop/.../sounds/' + sys.argv[1]).normalize()

"""
Poop labels
-----------

27000-49000 poop1.wav
47000-70000 poop2.wav

"""

s = 25000
e = 40000
r = 1000

fig, ax = plt.subplots()
l, = plt.plot(0,0,'.')
plt.axis([-400,400,-400,400])
# t = ax.text(7,7,'')



axamp = plt.axes([0.25, .03, 0.50, 0.02])
samp = Slider(axamp, 'Amp', 0, e-s, valinit=0)

def update(val):
    v = int(val)
    new_data = np.fft.fft(s0.data[s+v:s+v+r])
    # t.set_text(np.linalg.norm(new_data))
    l.set_data(new_data.real, new_data.imag)
    fig.canvas.draw_idle()

samp.on_changed(update)

plt.show()