import numpy as np
import matplotlib.pyplot as plt

from resource import Resource
from imageio import imread, imsave


img_res = Resource(('../data/images/', 'mom', 'jpg'))

image = imread(img_res.string)
h,w,d = image.shape

rand_pix = np.random.randint(h), np.random.randint(w)

print(rand_pix)
