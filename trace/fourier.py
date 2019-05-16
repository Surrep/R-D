import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.misc import imread, imsave


class Resource:
    def __init__(self, attrs, stub='%s%s.%s'):
        self.stub = stub
        self.attrs = attrs
        self.string = self.stub % self.attrs


b = 8
p = 1.0

bin_res = Resource(('../data/bins/', '12', 'txt'))
img_res = Resource(('../data/images/', 'mom', 'jpg'))

image = imread(img_res.string)
bins = np.array(pd.read_csv(bin_res.string, header=None)[0])

image_binned = bins[image.dot([256 ** 2, 256 ** 1, 256 ** 0])]
image_bincounts = np.bincount(image_binned.reshape(-1))
dense_region = np.argsort(image_bincounts)[b]
image_density_map = image_binned == dense_region

w, h = map(lambda d: int(d / 2), image_binned.shape)
grid = np.meshgrid(range(-h, h), range(-w, w))

coords = np.vstack(map(lambda a: a[image_density_map], grid)).T.astype(float)
coords[:, 0] /= h
coords[:, 1] /= w

path = coords[np.random.choice(a=[True, False],
                               size=coords.shape[0],
                               p=[p, 1 - p])].view(complex)

plt.plot(path.real, -path.imag, '.')
plt.show()
