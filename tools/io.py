import os
import string
import subprocess
import numpy as np

from scipy.io.wavfile import read, write


def abs_path(path):
    return os.path.abspath(path)


def join_paths(*paths):
    return os.path.join(*paths)


def specread_dir(dir_path, num_files=None):
    abs_dir_path = abs_path(dir_path)
    abs_file_paths = os.listdir(abs_dir_path)[:num_files]

    return np.stack([
        specread(join_paths(abs_dir_path, path))
        for path in abs_file_paths
    ], axis=0)


def sndread_dir(dir_path, num_files=None):
    abs_dir_path = abs_path(dir_path)
    abs_file_paths = os.listdir(abs_dir_path)[:num_files]

    samples = []
    for path in abs_file_paths:
        sample_rate, sample = sndread(join_paths(abs_dir_path, path))

        align_ratio = int(np.ceil(sample.size / sample_rate))
        aligned_sample = np.zeros(align_ratio * sample_rate)
        aligned_sample[:sample.size] = sample

        samples.append(aligned_sample)

    return np.vstack(tuple(samples))


def specread(path):
    return np.load(abs_path(path))


def sndread(path):
    sample_rate, signal = read(abs_path(path))
    signal = signal.astype(float) / np.abs(signal).max()

    return sample_rate, signal


def play(data, fs=44100):
    write('./data/output.wav', fs, data)
    subprocess.call(["afplay", './data/output.wav'])
