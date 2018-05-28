import numpy as np


class MetaNet():
    """
        This network deals with all hyperparameters
    """

    def __init__(self, X_shape, y_shape=None, neurons=1000):
        self.X_shape = X_shape
        self.y_shape = y_shape
        self.neurons = neurons

        network = self.gen_network(self.X_shape)
        wires = self.gen_wiring(network, self.X_shape)

    def gen_synapse(self, size, constraints):
        root = np.power(size, 1 / len(constraints))
        shape = [min(constraint, root) for constraint in constraints]

        return tuple([1 + np.random.randint(dim) for dim in shape])

    def gen_network(self, constraints):
        network = list()
        contact_points = np.prod(constraints)

        while contact_points:
            synapse_shape = self.gen_synapse(contact_points, constraints)
            contact_points -= np.prod(synapse_shape)
            network.append(synapse_shape)

        return network

    def gen_wiring(self, network, constraints):
        indices = np.array([np.ravel(i) for i in np.indices(constraints)]).T
        valid_tuples = [tuple(index) for index in indices]

        
