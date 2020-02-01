import numpy as np

weights = -0.5
inputs = 0.4
target = 0.3


alpha = 0.1

for it in range(100):
    # Weights determine the relationship between input and output
    prediction = weights * inputs

    # How `off` is that relationship
    delta = prediction - target

    # Square the error - to punish big misses more
    error = delta ** 2

    # How do we change the weights to match the output
    gradient = 2 * delta * inputs

    # Once we know the proper direction to move, take a step
    weights -= alpha * gradient

    # Print our progress
    if not (it % 10):
        print(error)
