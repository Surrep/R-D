import numpy as np

# Initialize
train_lights = np.array([
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 1],
    [1, 1, 1],
])

weights = np.random.randn(3, 1)
walk_or_stop = np.array([10, 10, 0, 0]).reshape(4, 1)

alpha = 0.01

# Train
for i in range(int(1e4)):
    prediction = train_lights.dot(weights)
    delta = prediction - walk_or_stop
    error = np.linalg.norm(delta)
    gradient = train_lights.T.dot(delta)

    weights -= alpha * gradient

    if not i % 1000:
        print(error)
