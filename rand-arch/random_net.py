import numpy as np


class RandomNeuralNetwork():

    def __init__(self, X, y=None,
                 neurons=1000, kinesis=1):
        self.X = X
        self.y = y
        self.neurons = neurons
        self.kinesis = kinesis

        self.input_scaffold = self.gen_scaffold(X)

    def gen_layer_dims(self, size, depth):
        return tuple([
            np.random.randint(np.power(size, 1 / depth)) + 1
            for _ in range(depth)
        ])

    def get_indices(self, shape):
        index_grid = np.indices(shape)
        count = np.prod(shape)
        indices = np.vstack([
            index_grid[i].ravel() for i in range(len(index_grid))
        ]).T

        return indices, count

    def gen_scaffold(self, data):
        indices, i_count = self.get_indices(data.shape)
        random_indices = list(np.random.choice(i_count, i_count, False))

        layers = []
        while i_count:  # while there is data left to group
            feed_size = np.random.randint(i_count) + 1
            dims = self.gen_layer_dims(size=feed_size, depth=len(data.shape))

            layer_size = np.prod(dims)
            layer = np.array([random_indices.pop() for _ in range(layer_size)])
            layers.append(layer.reshape(dims))

            i_count -= layer_size

        return layers
