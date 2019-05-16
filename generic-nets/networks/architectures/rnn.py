import numpy as np


class RNN:

    def __init__(self, layers, X, y, activation, loss,
                 sequence_len=30, lr=1e-6):

        self.params = {
            'X': X,
            'y': y
        }

        self.grads = {}
        self.activation = activation
        self.loss_fn = loss
        self.num_layers = len(layers)
        self.lr = lr
        self.sequence_len = sequence_len

        for l in range(1, self.num_layers):
            layer = 'W' + str(l)
            self.params[layer] = np.random.randn(layers[l - 1], layers[l])

    def loss(self):
        loss = 0
        for t in range(self.params['X'].shape[1]):
            y_layer = 'Y' + str(t)
            yhat = self.params[y_layer]
            yt = self.params['X'][:, t:self.sequence_len + t]

            if yt.shape[1] < self.sequence_len:
                yt = np.append(yt, np.repeat(
                    0, self.sequence_len - yt.shape[1]))

            loss += self.loss_fn(yhat, yt)

        return loss

    def forward(self, X=None):
        X = self.params['X'] if X is None else X
        XH = self.params['W1']
        HH = self.params['W2']
        HY = self.params['W3']

        # first hidden vec
        self.params['H-1'] = np.zeros((HH.shape[0]))
        for t in range(X.shape[1]):
            xt = self.params['X'][:, t:self.sequence_len + t]
            if xt.shape[1] < self.sequence_len:
                xt = np.append(xt, np.repeat(
                    0, self.sequence_len - xt.shape[1]))

            zx = xt.dot(XH)
            h_prev = self.params['H' + str(t - 1)]
            zh = h_prev.dot(HH)
            a_total = self.activation(zx + zh)
            yhat = a_total.dot(HY)

            h_layer = 'H' + str(t)
            y_layer = 'Y' + str(t)

            self.params[h_layer] = a_total
            self.params[y_layer] = yhat

    def backward(self, gradient_check=False):
        XH = self.params['W1']
        HH = self.params['W2']
        HY = self.params['W3']

        for t in range(self.params['X'].shape[1]):
            y_layer = 'Y' + str(t)
            h_layer = 'H' + str(t)

            ah = self.params[h_layer]
            yhat = self.params[y_layer]
            yt = self.params['y'][:, t:self.sequence_len + t]

            if yt.shape[1] < self.sequence_len:
                yt = np.append(yt, np.repeat(
                    0, self.sequence_len - yt.shape[1]))

            dy = yhat - yt
            dhy = ah.T.dot(dy)
            dah = dy.dot(HY.T)
            

            break

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

    def train(self, iters=10000):
        for i in range(iters):
            self.forward()
            if not i % 2500:
                print(i, self.loss())
            self.backward()

    def predict(self, X):
        self.forward(X)

        return self.params['Z' + str(self.num_layers - 1)]
