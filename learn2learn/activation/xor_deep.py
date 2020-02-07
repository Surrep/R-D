import numpy as np
from ..utilities.activations import relu, drelu

# Inputs
train_lights = np.array([
    [1, 0, 0, 1],
    [0, 1, 0, 1],
])

# Weights
weights_0_1 = np.random.randn(3, 2)
weights_1_2 = np.random.randn(1, 3)

# Initial Weights
weights_0_1_init = weights_0_1.copy()
weights_1_2_init = weights_1_2.copy()

# Labels
walk_or_stop = np.array([5, 5, 0, 0])

# Parameters
alpha = 0.0001

# Train
for i in range(int(1e5)):
    # Forward Layers
    layer_0 = train_lights
    layer_1 = relu(weights_0_1.dot(layer_0))
    layer_2 = weights_1_2.dot(layer_1)

    # Error
    layer_2_delta = layer_2 - walk_or_stop
    layer_1_delta = weights_1_2.T.dot(layer_2_delta) * drelu(layer_1)

    error = np.linalg.norm(layer_2_delta) + np.linalg.norm(layer_1_delta)

    # Gradient
    weights_1_2_gradient = layer_2_delta.dot(layer_1.T)
    weights_0_1_gradient = layer_1_delta.dot(layer_0.T)

    # Descent
    weights_1_2 -= alpha * weights_1_2_gradient
    weights_0_1 -= alpha * weights_0_1_gradient

    if not i % 1000:
        print(error)

# Save Weights
base_file_path = './{}'.format('/'.join(__name__.split('.')[:-1]))
div_file_path = '{}/{}'.format(base_file_path, 'weights_diverged.npz')
conv_file_path = '{}/{}'.format(base_file_path, 'weights_converged.npz')

file_name = conv_file_path if error < 1 else div_file_path
file_handle = open(file_name, 'a')

np.savez(file_name,
         weights_0_1_init, weights_0_1,
         weights_1_2_init, weights_1_2)

