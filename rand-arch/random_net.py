import numpy as np


class RandomNeuralNetwork():

    def __init__(self, X, y=None,
                 neurons=1000, kinesis=1,
                 mutation_rate=0.01):
        self.X = X
        self.y = y
        self.neurons = neurons
        self.kinesis = kinesis
        self.mutation_rate = [mutation_rate, 1 - mutation_rate]

        self.input_scaffold, self.gene_pool = self.gen_scaffold(X)
        self.connections = self.gen_connections()
        self.input_data = self.feed(self.input_scaffold, self.X.reshape(-1))

        print(self.connections)

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

        layers = list()
        gene_pool = list()
        while i_count:  # while there is data left to group
            feed_size = np.random.randint(i_count) + 1
            dims = self.gen_layer_dims(size=feed_size, depth=len(data.shape))

            layer_size = np.prod(dims)
            layer = np.array([random_indices.pop() for _ in range(layer_size)])
            layers.append(layer.reshape(dims))

            gene_pool.extend(dims)

            i_count -= layer_size

        return layers, set(gene_pool)

    def gen_mutation(self, env_size):
        mutation = np.random.randint(np.sqrt(env_size))
        mutation_occured = np.random.choice([1, 0], p=self.mutation_rate)

        return mutation, mutation_occured

    def gen_connections(self):
        connections = list()
        remaining_neurons = self.neurons
        while remaining_neurons > 0:
            mutation, mutation_occurred = self.gen_mutation(remaining_neurons)
            if mutation_occurred:
                self.gene_pool.add(mutation)

            gene_1 = np.random.choice(list(self.gene_pool))
            gene_2 = np.random.choice(list(self.gene_pool))

            conn_matrix = np.ones((gene_1, gene_2)) / self.neurons
            connections.append(conn_matrix)

            remaining_neurons -= gene_1 * gene_2

        return connections

    def forward(self):
        pass

    def feed(self, scaffold, data):
        return [data[layer] for layer in scaffold]
