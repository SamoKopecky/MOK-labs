import numpy as np
import numpy.random as rand


def create(seed, dim, mod):
    np.random.seed(seed)
    matrix = rand.randint(-mod, mod, (dim, dim))
    vector = rand.randint(-mod, mod, dim)
    return matrix.dot(vector) % mod


print(create(6, 20, 10))
