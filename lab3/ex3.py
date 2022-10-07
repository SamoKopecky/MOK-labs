import numpy as np
from numpy.polynomial import polynomial as poly
from numpy.polynomial import Polynomial as P
from utils import random_poly
from ex1 import polyadd_mod
from ex2 import polymul_mod


def kem(seed, dim, modulus, poly_mod):
    A = random_poly(modulus, modulus**2, seed)
    e = np.random.normal(0, 2, size=dim) % modulus
    s = np.random.randint(0, 2, size=dim)
    print(A)
    print(e)
    print(s)
    first = polymul_mod(-A, s, modulus, poly_mod)
    print(first)
    return polyadd_mod(first[0], -e, modulus, poly_mod)


def main():
    print(kem(2, 4, 5, np.array([1, 0, 1])))


if __name__ == "__main__":
    main()
