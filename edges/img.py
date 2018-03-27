from scipy.misc import imsave, imread
from colors import binitize, random_color

import numpy as np
import sys

module, img_name = sys.argv

bins = 8
image = binitize(imread('/Users/tru/Desktop/photos/{}.jpg'.format(img_name)))
out = np.zeros((*image.shape, 3))

for color in range(bins):
    out[image == color] = random_color()


imsave('/Users/tru/Desktop/out{}.jpg'.format(bins), out)
