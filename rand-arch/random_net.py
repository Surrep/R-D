import numpy as np


class RandomNeuralNetwork():

    def __init__(self, X, y=None,
                 neurons=1000):
        self.X = X
        self.y = y
        self.neurons = neurons

    def gen_random_layer(self, shape):
        return tuple([
            np.random.randint(shape[i]) + 1
            for i in range(len(shape))
        ])

    def gen_synapse(self, size, constraints):
        root = np.power(size, 1 / len(constraints))
        shape = [min(constraint, root) for constraint in constraints]

        return tuple([1 + np.random.randint(dim) for dim in shape])

    def gen_network(self, data):
        synapses = list()
        contact_points = np.prod(data.shape)

        while contact_points:
            synapse_shape = self.gen_synapse(contact_points, data.shape)
            contact_points -= np.prod(synapse_shape)
            synapses.append(synapse_shape)

        return synapses


rnn = RandomNeuralNetwork(np.random.rand(100, 1))
print(rnn.gen_network(rnn.X))
