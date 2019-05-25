import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from resource import Resource
from imageio import imread, imsave


img_res = Resource(('../data/images/', 'shoo_fly', 'jpg'))
image = imread(img_res.string)

mask_size = 0 # must be less than half of image size in both dimensions

rr,rc = np.random.randint(mask_size, image.shape[0] - mask_size), \
        np.random.randint(mask_size, image.shape[1] - mask_size)

mask = slice(-mask_size + rr, mask_size + rr), \
       slice(-mask_size + rc, mask_size + rc)

m_image = image[mask] if mask_size else image
imsave('test.jpg', m_image)

r,g,b = m_image[:,:,0].reshape(-1), \
        m_image[:,:,1].reshape(-1), \
        m_image[:,:,2].reshape(-1)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
ax.scatter(r,g,b,c=m_image.reshape(-1,3) / 255)

plt.show()


