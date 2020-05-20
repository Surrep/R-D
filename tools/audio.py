import math
import numpy as np


def wheel(k, n, sample_rate=44100):
    real = np.cos(2 * np.pi * k * n / sample_rate)
    imag = np.sin(2 * np.pi * k * n / sample_rate)

    return real - 1j*imag


def dft(signal, freqs, sample_rate=44100):
    len_freqs = len(freqs)
    len_signal = len(signal)

    spectrogram = np.zeros((len_freqs, len_signal), complex)

    for si in range(len_signal):
        for ki, k in enumerate(freqs):
            spectrogram[ki, si] = wheel(k, si, sample_rate) * signal[si]

    return spectrogram


def real_spectrogram(signal, num_freqs, skip=1):
    num_freqs_adjusted = num_freqs * 2 - 1
    num_samples_adjusted = math.ceil(len(signal) / skip)

    result = np.zeros((num_freqs, num_samples_adjusted), complex)

    for i, si in enumerate(range(0, len(signal), skip)):
        samples = signal[si:si+num_freqs_adjusted]
        result[:, i] = np.fft.rfft(samples, num_freqs_adjusted)

    return result


def real_inv_spectrogram(spectrogram):
    num_freqs, num_samples = spectrogram.shape

    result = np.zeros(num_samples + num_freqs * 2)

    for si in range(num_samples):
        samples = np.fft.irfft(spectrogram[:, si])
        result[si:si+samples.size] = samples

    return result


def sinusoid(frequency=440, sample_rate=44100, duration=1):
    return np.sin(np.linspace(0,
                              2 * np.pi * frequency * duration,
                              duration * sample_rate))


def transform(data):
    coefficients = np.fft.rfft(data)
    spectrum = np.abs(coefficients)
    sorted_idx = np.argsort(-spectrum)

    return coefficients, spectrum, sorted_idx
