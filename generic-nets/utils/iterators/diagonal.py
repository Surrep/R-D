from utils.misc.bound_check import in_bounds
import numpy as np


class IterDiag():

    def __init__(self, shape):
        self.shape = shape
        self.rows = self.shape[0]
        self.cols = self.shape[1]
        self.diagonals = np.sum(self.shape) - 1

    def get_starting_coord(self, diag):
        if diag % 2:
            return (max(0, diag - (self.cols - 1)),
                    min(self.cols - 1, diag))
        else:
            return (min(self.rows - 1, diag),
                    max(0, diag - (self.rows - 1)))

    def generate_diagonals(self):
        for diag in range(self.diagonals):
            r, c = self.get_starting_coord(diag)
            while in_bounds(self.shape, r, c):
                yield (r, c)
                r += 1 if diag % 2 else -1
                c += 1 if not diag % 2 else -1
