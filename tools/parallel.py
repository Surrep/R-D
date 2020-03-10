"""

Parallel Processing Code Under Construction

"""
# import multiprocessing as mp
# from multiprocessing import sharedctypes

# frequencies = range(500)

# template = np.ctypeslib.as_ctypes(np.zeros((len(frequencies), len(signal))))
# shared_spectrum = sharedctypes.RawArray(template._type_, template)


# def spectrogram(frequency):
#     ki, k = frequency
#     tmp = np.ctypeslib.as_array(shared_spectrum)

#     for si in range(len(signal)):
#         coefficient = dft_point(k, si, sample_rate) * signal[si]
#         tmp[ki, si, 0] = coefficient.real
#         tmp[ki, si, 1] = coefficient.imag


# def spectrogram_cum(frequency):
#     ki, k = frequency
#     tmp = np.ctypeslib.as_array(shared_spectrum)

#     for si in range(len(signal)):
#         previous = np.array([0, 0]) if not si else tmp[ki, si - 1]

#         coefficient = dft_point(k, si, sample_rate) * signal[si]
#         tmp[ki, si, 0] = previous[0] + coefficient.real
#         tmp[ki, si, 1] = previous[1] + coefficient.imag


# pool = mp.Pool(mp.cpu_count())

# for i, _ in enumerate(pool.imap(spectrogram_cum, enumerate(frequencies))):
#     print('\rdone {0:%}'.format(i/len(frequencies)))

# spectrum = np.ctypeslib.as_array(shared_spectrum).view(complex)[:, :, 0]

# pool.close()


# def show_mag(spectrogram):
#     plt.imshow(np.abs(spectrogram), aspect='auto')
#     plt.colorbar()
#     plt.show()


# def show_phase(spectrogram):
#     plt.imshow(np.angle(spectrogram), aspect='auto')
#     plt.colorbar()
#     plt.show()
