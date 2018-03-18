from scipy.misc import imsave

import skvideo.io
import numpy as np
import pandas as pd


def random_color():
    return np.random.randint(0, 256, (3))


colors = 2
path = '/Users/tru/Desktop/photos/gsw.mp4'
color_bins = '/Users/tru/Workspace/recognition/data/colorBins{}.txt'.format(
    colors)

identifier = [256 ** 2, 256 ** 1, 256 ** 0]
bins = np.array(pd.read_csv(color_bins, header=None)[0])
color_scheme = [random_color() for color in range(colors)]

# videodata = skvideo.io.vread(path)
video = skvideo.io.vreader(path)
frame_zero = next(video)
out_video = np.zeros((2000, *frame_zero.shape))

# imsave("/Users/tru/Desktop/photos/lic.jpg",frame_zero)


def colorize_frame(frame):
    low_res = bins[frame.dot(identifier)]
    color_frame = np.zeros(frame.shape)

    for cid in range(colors):
        color_frame[low_res == cid] = color_scheme[cid]

    return color_frame


for i, frame in enumerate(video):
    c_frame = colorize_frame(frame)
    if i < out_video.shape[0]:
        out_video[i] = c_frame
    else:
        break


skvideo.io.vwrite(
    "/Users/tru/Desktop/outputvideo{}.mp4".format(colors), out_video)
