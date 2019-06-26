import numpy as np


class BaseNet:

    def __init__(self, layers, X, y, activation, loss, lr=1e-6):

        self.params = {
            'X': X,
            'y': y
        }

        self.grads = {}
        self.activation = activation
        self.loss_fn = loss
        self.num_layers = len(layers)
        self.lr = lr

    def forward(self, X=None):
        pass  # abstract

    def backward(self, gradient_check=False):
        pass  # abstract

    def grad_check(self, grad_guess, layer, h=0.00001):
        weight_mat = self.params[layer]
        num_grad = np.zeros_like(weight_mat)
        it = np.nditer(weight_mat, flags=[
            'multi_index'], op_flags=['readwrite'])

        while not it.finished:
            ix = it.multi_index
            old_val = weight_mat[ix]

            weight_mat[ix] += h
            self.forward()
            pos = self.loss()

            weight_mat[ix] = old_val

            weight_mat[ix] -= h
            self.forward()
            neg = self.loss()

            weight_mat[ix] = old_val
            self.forward()

            num_grad[ix] = (pos - neg) / (2 * h)
            it.iternext()

        print(layer, np.linalg.norm(grad_guess - num_grad) /
              np.linalg.norm(grad_guess + num_grad))

    def loss(self):
        yhat = self.params['Z' + str(self.num_layers - 1)]

        return self.loss_fn(yhat, self.params['y'])

    def train(self, iters=10000):
        for i in range(iters):
            self.forward()
            if not i % 2500:
                print(i, self.loss())
            self.backward()

    def predict(self, X):
        self.forward(X)

        return self.params['Z' + str(self.num_layers - 1)]
