#!/usr/bin/python

import numpy as np
import random

VERBOSE = 0


# Reload a file:
# import importlib
# importlib.reload()

# Predefined functions

# Compute the hamdamard ratio of matrix "basis"
# This function is used to determine how orthogonal the matrix is
#	close to 1 = orthogonal
#	close to 0 = parallel vectors

def hamdamard_ratio(basis):
    dimension = basis.ndim
    detOfLattice = np.linalg.det(basis)
    mult = 1
    for v in basis:
        mult = mult * np.linalg.norm(v)  # (np.sqrt((v.dot(v))))
    hratio = (detOfLattice / mult) ** (1.0 / dimension)
    return hratio


# Compute an unimodular matrix, i.e. a matrix of det = +-1,
# that can be multiplied to a good basis (private key) to create a bad bases (public key).

def rand_unimod(seed, n):
    np.random.seed(seed)
    random.seed(seed)
    random_matrix = [[np.random.randint(-10, 10, ) for _ in range(n)] for _ in range(n)]
    upperTri = np.triu(random_matrix, 0)
    lowerTri = [[np.random.randint(-10, 10) if x < y else 0 for x in range(n)] for y in range(n)]

    for r in range(len(upperTri)):
        for c in range(len(upperTri)):
            if (r == c):
                if bool(random.getrandbits(1)):
                    upperTri[r][c] = 1
                    lowerTri[r][c] = 1
                else:
                    upperTri[r][c] = -1
                    lowerTri[r][c] = -1
    uniModular = np.matmul(upperTri, lowerTri);
    return uniModular


#  Babai’s Closest Vertex Algorithm.
#  It permits to solve the closest vector to "vector" in the lattice "basis".

def babai(basis, vector):
    dimension = basis[0].size
    if VERBOSE == 1:
        print('dimension of the vector', dimension)
    inv = np.linalg.inv(basis)
    t_vect = vector.dot(inv)
    t_round = np.round(t_vect)
    if VERBOSE == 1:
        print('Vector t = ', t_vect)
    b_vector = np.zeros(dimension)
    for i in range(len(basis)):
        b_vector = b_vector + t_round[i] * basis[i]
        if VERBOSE == 1:
            print(t_round[i] * basis[i])
    return b_vector
