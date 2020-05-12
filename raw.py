from tools.loaders import SpeechCommands

# Load Raw
raw_samples = SpeechCommands.load_raw(words=['yes', 'up', 'right', 'follow'],
                                      num_files=100,
                                      as_tf=False)

mean_sample = raw_samples.mean(axis=0)
zero_centered_samples = raw_samples - mean_sample

# PCA
U, E, Vt = np.linalg.svd(zero_centered_samples)
