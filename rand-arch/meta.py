import numpy as np


class MetaSynapse():
    def __init__(self, max_size, constraints, contact_points):
        root = np.power(max_size, 1 / len(constraints))
        shape = [min(constraint, root) for constraint in constraints]

        self.constraints = constraints
        self.shape = tuple([1 + np.random.randint(dim) for dim in shape])
        self.size = np.prod(self.shape)

        length = None if max_size == self.size else max_size - self.size - 1
        self.contact_points = contact_points[slice(max_size - 1, length, -1)]


class MetaNet():
    """
        This network deals with all hyperparameters
    """

    def __init__(self, X_shape, y_shape=None):
        self.X_shape = X_shape
        self.y_shape = y_shape
        self.network = list()

        indices = np.array([np.ravel(i) for i in np.indices(self.X_shape)]).T
        np.random.shuffle(indices)

        remaining_data = np.prod(self.X_shape)
        while remaining_data:
            synapse = MetaSynapse(remaining_data, self.X_shape, indices)
            remaining_data -= synapse.size
            self.network.append(synapse)
