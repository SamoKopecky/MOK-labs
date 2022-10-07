import numpy as np
from numpy.polynomial import polynomial as poly
from utils import random_poly


def polyadd_mod(y, z, mod, poly_mod):
    result = poly.polyadd(y, z) % mod
    return poly.polydiv(result, poly_mod)


def main():
    modulo = 11
    seed = 8

    r = np.array([1, 0, 1])
    p1 = random_poly(modulo, 5, 8)
    p2 = random_poly(modulo, 5, 3459)

    print(p1)
    print(p2)
    print(polyadd_mod(p1, p2, modulo, r))


if __name__ == "__main__":
    main()
