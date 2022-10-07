import numpy as np


def random_poly(mod, size, seed):
    np.random.seed(seed)
    return np.random.randint(low=-mod + 1, high=mod - 1, size=size)
