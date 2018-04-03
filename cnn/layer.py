from scipy.misc import imread, imsave
import numpy as np

photo_repo = '/Users/tru/Desktop/photos/'

photo = imread(photo_repo + 'drt.jpg')
rows, cols, channels = photo.shape

maps = 1
L1 = np.random.randn(5, 5, 3, maps)
receptive_field = np.arange(-2, 3)

out = np.zeros((rows, cols, maps))

margin = 5
stride = 2

for r in range(margin, rows - margin, stride):
    for c in range(margin, cols - margin, stride):
        for i in range(maps):
            field = np.ix_(receptive_field + r, receptive_field + c)
            activation = (photo[field] * L1[:, :, :, i]).sum()
            out[r, c, i] = activation

for filt in range(maps):
    imsave('/Users/tru/Desktop/out{}.jpg'.format(filt), out[:, :, filt])
