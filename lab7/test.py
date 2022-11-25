import ex1
import ex2

import pytest
import random

@pytest.mark.parametrize(
    "secret,degree,n,q",
    [
        (5, 2, 3, 11),
        (13, 11, 12, 19),
        (8, 15, 18, 23),
        (73, 25, 26, 103),
    ],
)
def test_reconstruct_secret(secret: int, degree: int, n: int, q: int):
    poly = ex1.gen_poly(secret, degree, q)

    shares = ex1.create_shares(n, poly, q)

    while len(shares) - 1 > degree:
        shares.pop(random.randint(0, len(shares) - 1))

    reconstructed = ex1.reconstruct_secret(shares, degree, q)

    assert secret == reconstructed

@pytest.mark.parametrize(
    "secret,degree,n,q",
    [
        (5, 2, 3, 11),
        (13, 11, 12, 19),
        (8, 15, 18, 23),
        (58, 100, 101, 103),
    ],
)
def test_reconstruct_secret_interpolation(secret: int, degree: int, n: int, q: int):
    poly = ex1.gen_poly(secret, degree, q)

    shares = ex1.create_shares(n, poly, q)

    while len(shares) - 1 > degree:
        shares.pop(random.randint(0, len(shares) - 1))

    reconstructed = ex2.reconstruct_secret(shares, q)

    assert secret == reconstructed