import numpy as np


class FCN:

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

        for l in range(1, self.num_layers):
            self.params['W' + str(l)
                        ] = np.random.randn(layers[l - 1], layers[l])

    def forward(self, X=None):
        X = self.params['X'] if X is None else X
        for l in range(self.num_layers - 1):
            al = self.params['A' + str(l)] if l > 0 else X
            wl = self.params['W' + str(l + 1)]
            zl = al.dot(wl)

            self.params['Z' + str(l + 1)] = zl
            self.params['A' + str(l + 1)] = self.activation(zl)

    def backward(self, gradient_check=False):
        y = self.params['y']
        yhat = self.params['Z' + str(self.num_layers - 1)]
        self.grads['Z' + str(self.num_layers - 1)] = yhat - y

        for l in range(self.num_layers - 1, 0, -1):
            if l > 1:
                al_prev = self.params['A' + str(l - 1)]
                zl_prev = self.params['Z' + str(l - 1)]
            else:
                al_prev = self.params['X']

            wl = self.params['W' + str(l)]
            dzl = self.grads['Z' + str(l)]

            dwl = al_prev.T.dot(dzl)
            self.grads['W' + str(l)] = dwl
            if l > 1:
                dal_prev = dzl.dot(wl.T)
                dzl_prev = dal_prev.copy()
                dzl_prev[zl_prev < 0] = 0

                self.grads['Z' + str(l - 1)] = dzl_prev

            if gradient_check:
                self.grad_check(grad_guess=dwl, layer='W' + str(l))

        # Update weights
        for param in self.params:
            if param.startswith("W"):
                self.params[param] -= self.lr * self.grads[param]

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
