import numpy as np
import pandas as pd
import os

from scipy.misc import imread

identifier = [256 ** 2, 256 ** 1, 256 ** 0]
bins = np.array(pd.read_csv(
    '/Users/tru/Workspace/surrep/recognition/data/colorBins2.txt', header=None)[0])


def write_map(path):
    f = imread(path)

    name, ext = os.path.splitext(os.path.basename(path))
    write_path = '/Users/tru/Desktop/texts/{}.txt'.format(name)

    np.savetxt(write_path, bins[f.dot(identifier)].reshape(-1), fmt="%d")
    print(*f.shape, file=open(write_path, 'a'))
