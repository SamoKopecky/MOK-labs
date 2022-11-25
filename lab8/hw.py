import random
from typing import List

import numpy as np
import sympy as sp


def gen_poly(secret: int, degree: int, q: int) -> List[int]:
    """Generate polynomial with secret.

    :param secret: Secret that should be used in polynomial.
    :param degree: Degree of polynomial.
    :param q: Coefficients modulus.
    :return: Generated polynomial.
    """
    numbers = np.random.randint(low=0, high=q, size=degree + 1)
    numbers[degree] = secret
    return numbers.tolist()


def create_shares(n: int, poly: List[int], q: int) -> List[tuple[int, int]]:
    """Create shares that represent polynomial.

    :param n: Number of shares that should be created.
    :param poly: Unique polynomial used to create shares.
    :param q: Coefficients modulus.
    :return: List of x values and its polynomial evaluations.
    """
    x = sp.symbols("x")
    sp_poly = sp.Poly(poly, x)
    return [(i + 1, sp_poly.eval(i + 1) % q) for i in range(n)]


class Tallier:
    def __init__(self, secret):
        self.secret = secret
        self.shares = []
        self.private_key = 0

    def calculate_private_key(self, p):
        for share in self.shares:
            self.private_key = (share[1] + self.private_key) % p


def reconstruct_secret(shares: List[tuple[int, int]], q: int) -> List[int]:
    """Reconstruct secret from provided shares.

    :param shares: Secret that should be used in polynomial.
    :param q: Coefficients modulus.
    :return: Reconstructed secret.
    """
    secrets = []
    for i in range(len(shares)):

        yi = shares[i][1]
        xi = shares[i][0]
        temp = yi
        for j in range(len(shares)):
            if j == i:
                continue
            temp *= shares[j][0] * pow((shares[j][0] - xi) % q, -1, q) % q
        secrets.append(temp % q)
    return secrets


def encrypt(h, p, v, g):
    r = random.randint(0, p) % p
    e = pow(g, r, p), (pow(h, r, p) * pow(g, v, p)) % p
    return e, r


def main():
    p, g, q, t, n = 31, 3, 30, 5, 5
    secrets = [2, 3, 5, 1, 7]
    h_parts = [pow(g, secrets[i], p) for i in range(n)]
    h = 1
    for i in range(len(h_parts)):
        h = (h_parts[i] * h) % p
    polys = [gen_poly(secrets[i], t - 1, p) for i in range(n)]
    talliers = [Tallier(secrets[i]) for i in range(n)]
    for i in range(n):
        share = create_shares(n, polys[i], p)
        for j in range(len(talliers)):
            talliers[j].shares.append(share[j])

    [tallier.calculate_private_key(p) for tallier in talliers]
    votes = [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1]
    c1, c2 = 1, 1
    r_sum = 0
    for i in range(len(votes)):
        c, r = encrypt(h, p, votes[i], g)
        c1 = (c1 * c[0]) % p
        c2 = (c2 * c[1]) % p
        r_sum += r

    sum_shares = []
    for i in range(t):
        second = 0
        for j in range(t):
            second += talliers[i].shares[j][1]
        sum_shares.append((i + 1 % p, second % p))
    lambdas = reconstruct_secret(sum_shares, p)
    print(sum(secrets), sum(lambdas) % p)
    d = 1
    for i in range(t):
        d_i = int(pow(c1, int(talliers[i].private_key), p))
        l_i = int(lambdas[i])
        d = (d * pow(d_i, l_i, p)) % p

    left_side = pow(g, sum(votes), p)
    right_side = (pow(d, -1, p) * c2) % p
    print(f"d-1c2 = {right_side}, g^sum votes = {left_side}")


if __name__ == "__main__":
    main()
