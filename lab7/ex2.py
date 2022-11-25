from typing import List
import ex1


def reconstruct_secret(shares: List[tuple[int, int]], q: int) -> int:
    """Reconstruct secret from provided shares.

    :param shares: Secret that should be used in polynomial.
    :param q: Coefficients modulus.
    :return: Reconstructed secret.
    """
    secrets = 0
    for i in range(len(shares)):
        yi = shares[i][1]
        xi = shares[i][0]
        temp = yi
        for j in range(len(shares)):
            if j == i:
                continue
            temp *= shares[j][0] * inverse(shares[j][0] - xi, q) % q
        secrets += temp
    return secrets % q


def inverse(a, p):
    return pow(a, -1, p)


def main():
    degree = 100
    n = 101
    s = 58
    q = 103
    a = ex1.gen_poly(s, degree, q)
    shares = ex1.create_shares(n, a, q)
    print("secret", s)
    print("reconstructed", reconstruct_secret(shares, q))


if __name__ == "__main__":
    main()
