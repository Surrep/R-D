import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from scipy.misc import imread, imsave
np.set_printoptions(suppress=True, linewidth=1000, threshold=np.nan)

img = imread('/Users/tru/Desktop/flam.jpg')
rd = img.reshape(-1, 3)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter(rd[:, 0], rd[:, 1])
plt.show()
