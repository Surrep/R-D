
def gen_perturber(params):
    return np.zeros_like(params)


def perturb(params, perturber):
    [params + perturber, params - perturber]


def compute_grad(perturbations, epsilon):
    left, right = perturbations

    return (left - right) / (2 * epsilon)
