from perception.edges import EdgeFinder
from utils.misc.smartimage import SmartImage
from utils.misc.color import random_color

from scipy.misc import imsave

import time
import numpy as np

image_path = "/Users/tru/Desktop/photos/horsie.jpg"
image = SmartImage(image_path)

ef = EdgeFinder(image)

for color in range(32):
    print('writing', color)
    imsave('/Users/tru/Desktop/slices/clr{}.jpg'.format(color),
           ef.upstream.bins == color)
