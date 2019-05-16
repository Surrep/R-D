from utils.iterators.diagonal import IterDiag
import numpy as np

test = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

it = IterDiag(test.shape).generate_diagonals()

assert next(it) == (0, 0)
assert next(it) == (0, 1)
assert next(it) == (1, 0)
assert next(it) == (2, 0)
assert next(it) == (1, 1)
assert next(it) == (0, 2)
assert next(it) == (1, 2)
assert next(it) == (2, 1)
assert next(it) == (2, 2)
