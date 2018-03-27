import pandas as pd
import numpy as np

bin_path = '/Users/tru/Workspace/surrep/recognition/data/colorBins{}.txt'
identifier = [256 ** 2, 256 ** 1, 256 ** 0]


def random_color():
    return np.random.randint(0, 256, (3))


def binitize(image, bins=2):
    bins = np.array(pd.read_csv(bin_path.format(bins), header=None)[0])
    return bins[image.dot(identifier)]
