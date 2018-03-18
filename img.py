from scipy.misc import imsave, imread

import numpy as np
import pandas as pd

colors = 2

bins = np.array(pd.read_csv(
    '/Users/tru/Workspace/surrep/recognition/data/colorBins{}.txt'.format(colors), header=None)[0])

intensity = [0.2126, 0.7152, 0.0722]
identifier = [256 ** 2, 256 ** 1, 256 ** 0]


def random_color():
    return np.random.randint(0, 256, (3))


f = bins[imread('/Users/tru/Desktop/photos/house.jpg').dot(identifier)]
f2 = np.zeros((*f.shape, 3))

for color in range(colors):
    f2[f == color] = random_color()


imsave('/Users/tru/Desktop/funk{}.jpg'.format(colors), f2)
