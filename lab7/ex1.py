from typing import List
import random
import sympy as sp
import numpy as np

from math import gcd


def gen_poly(secret: int, degree: int, q: int) -> List[int]:
    """Generate polynomial with secret.

    :param secret: Secret that should be used in polynomial.
    :param degree: Degree of polynomial.
    :param q: Coefficients modulus.
    :return: Generated polynomial.
    """
    numbers = np.random.randint(low=0, high=q, size=degree + 1)
    numbers[degree] = secret
    return numbers


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


def reconstruct_secret(shares: List[tuple[int, int]], degree: int, q: int) -> int:
    """Reconstruct secret from provided shares.

    :param shares: Secret that should be used in polynomial.
    :param degree: Degree of polynomial.
    :param q: Coefficients modulus.
    :return: Reconstructed secret.
    """
    equations = []
    values = []
    for i in range(degree + 1):
        equations.append([shares[i][0] ** j % q for j in range(degree, -1, -1)])
        values.append(shares[i][1])
    result = solve_matrix(sp.Matrix(equations), sp.Matrix(values), q)
    return result[degree]


def solve_matrix(a: sp.Matrix, b: sp.Matrix, q: int) -> sp.Matrix:
    """Solve system of modular equations.
    :param a: NxN matrix.
    :param b: Nx1 matrix.
    :param q: Coefficient modulus.
    :return: Solution matrix.
    """
    det = int(a.det())
    if gcd(det, q) == 1:
        return pow(det, -1, q) * a.adjugate() @ b % q
    raise ValueError(f"Equation cannot be solved: det={det}.")


def main():
    degree = 2
    n = 4
    s = 4
    q = 11
    a = gen_poly(s, degree, q)
    shares = create_shares(n, a, q)
    print("secret", s)
    print("reconstructed", reconstruct_secret(shares, degree, q))


if __name__ == "__main__":
    main()
