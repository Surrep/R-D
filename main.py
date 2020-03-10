from tools.io import sndread_dir
from tools.plot import slide, animate, plot
from tools.sound import dft, sinusoid, transform

import numpy as np


sample_rate = 44100
signal = np.concatenate((
    sinusoid(frequency=200, duration=0.5),
    sinusoid(frequency=400, duration=0.5),
))

f, ps, idx = transform(signal)

spectrogram = dft(signal, idx[:8], sample_rate)
coefficients = np.fft.rfft(signal)


def slide_impl(data, time_step, lines, figure):
    time_step = int(time_step)

    coeffs = data[:, :time_step].cumsum(1)

    lines.set_data(coeffs.real, coeffs.imag)
    figure.canvas.draw_idle()


slide(spectrogram, slide_impl, range(len(signal)))
