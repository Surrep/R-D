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

start = 0
end = data.shape[0]
s = slice(start,end)

plt.plot(data[s], '.')
plt.show()