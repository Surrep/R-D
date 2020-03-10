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


def spectrogram(signal, freqs):
    len_freqs = len(freqs)
    len_signal = len(signal)

    result = np.zeros((len_freqs//2, len_signal), complex)

    for si in range(len_signal-len_freqs):
        result[:, si] = np.fft.rfft(signal[si:si+len_freqs])[:len_freqs//2]

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
