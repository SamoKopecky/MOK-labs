import numpy as np
import lattice as lt


def distance_lattice_vector(basis, vect):
    nearest_vector = lt.babai(basis, vect)
    dist = np.linalg.norm(np.abs(vect - nearest_vector))
    return dist


def better_basis(basis1, basis2, vect):
    dist1 = distance_lattice_vector(basis1, vect)
    dist2 = distance_lattice_vector(basis2, vect)
    if dist1 < dist2:
        print(f'{basis1} is better')
        return
    print(f'{basis2} is better')


seed = 200
np.random.seed(seed)

L = np.array([[4, 5], [8, 2]])
U = lt.rand_unimod(seed, 2)
B = np.matmul(L, U)
V = np.random.randint(-10, 10, 2)

print(distance_lattice_vector(L, V))

better_basis(L, B, V)
