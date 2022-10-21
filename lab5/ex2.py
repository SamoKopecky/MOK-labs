import numpy as np
from math import sqrt


def prime(a):
    if a < 2: return False
    for x in range(2, int(sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True


def random_prime(k):
    num = np.random.randint(low=0, high=k - 1, size=1)
    while not prime(num):
        num = np.random.randint(low=0, high=k - 1, size=1)
    return num


def encrypt(m, pk, n):
    return pow(m, pk, n)


def decrypt(c, sk, n):
    return pow(c, sk, n)


def check_homomorphism(sk, pk, n):
    m1 = 5
    m2 = 3
    m3 = m1 * m2
    c1 = encrypt(m1, pk, n)
    c2 = encrypt(m2, pk, n)

    print(f'm1: {m1}')
    print(f'm2: {m2}')

    print(f'c1: {c1}')
    print(f'c2: {c2}')

    c3 = encrypt(m1, pk, n) * encrypt(m2, pk, n)
    first = decrypt(c1, sk, n) * decrypt(c2, sk, n)
    second = decrypt(c3, sk, n)
    print(f'{m3} (m1 + m2) == {first} (dec(c1) * dec(c2))')
    print(f'{m3} (m1 + m2) == {second} (dec(c3))')


def main():
    k = 1000000
    p = int(random_prime(k))
    q = int(random_prime(k))
    n = p * q
    phi_n = (p - 1) * (q - 1)
    pk = 2 ** 16 + 1
    sk = pow(pk, -1, phi_n)

    print(f'n: {n}')
    print(f'p: {p}')
    print(f'q: {q}')
    print(f'sk: {sk}')
    print(f'pk: {pk}')

    check_homomorphism(sk, pk, n)


if __name__ == '__main__':
    main()
