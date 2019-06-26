from mpl_toolkits.mplot3d import Axes3D
from imageio import imread ,  imsave

import numpy as np
import matplotlib.pyplot as plt

def write_channels(ids ,  hist ,  path='/Users/trumanpurnell/Desktop/snaps/%s.jpg'):
    most_common_ids = hist.argsort()[::-1]
    for i in range(60):
        imsave(path % i ,  (ids == most_common_ids[i]).astype(int))


def create_hist(image):
    ids = img.dot([256 ** 2 ,  256 ,  1])
    hist = np.bincount(ids.ravel())

    return ids ,  hist

def qisect(image):
    if image.size == 1:
        return print(image)
    
    fr ,  fc = image.shape
    hr = fr // 2
    hc = fc // 2

    top_left = image[:hr ,  :hc]
    top_right = image[:hr ,  hc:]
    
    bot_left = image[hr: ,  :hc]
    bot_right = image[hr: ,  hc:]

    qisect(top_left )
    qisect(top_right)
    qisect(bot_left )
    qisect(bot_right)



img = imread('/Users/trumanpurnell/Desktop/lil.jpg')
ids, hist = create_hist(img)
