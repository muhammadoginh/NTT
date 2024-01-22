# Resource: 

import math
# from helper import *

# --- NTT functions ---

# Iterative NTT (Forward and Inverse)
# arrayIn = input polynomial
# P = modulus
# Y = 2nth root of unity (psi)
# inv = 0: forward NTT / 1: inverse NTT
# Input: Standard order/Output: Standard order


def iNTT(hatA, Y_table, q):
    '''
    iterative_radix2_gs_intt
    We refer to negacyclic convolution
    hatA : NTT form of A
    q    : Modulus
    Y_table : contains TF (2nth root of unity) constants in bit-reverse, 
    '''
    n = len(hatA)           # n - 1, Degree of polynomial,  which is the highest power of the variable in polynomial
    A = [x for x in hatA]   # A = iNTT(hatA)

    v = int(math.log2(n))
    # print("test")

    for i in range(v):
        for j in range(2**i):
            for k in range(n // 2**(i+1)):
                a_idx = j * n // (2 ** (i)) + k
                jump = n // (2 ** (i + 1))

                y = Y_table[((2 ** i) * k) % n]
                # y = Y_table[((2 ** i) + k)]
                # print("test")
                # print((2 ** i) + k)

                at_temp = (A[a_idx + jump] * y) % q

                A[a_idx + jump] = (hatA[a_idx] + at_temp) % q
                A[a_idx] = (hatA[a_idx] - at_temp) % q

    # hatA = indexReverse(hatA, v)
    return A


def NTT(A, Y_table, q):
    '''
    Iterative Radix-2 Cooley-Tukey Number Theoretic Transform (NTT)
    We refer to negacyclic convolution
    A : Polynomial in coefficient form
    q : Modulus
    Y_table : contains TF (2nth root of unity) constants in bit-reverse, 
    '''
    n = len(A)        # n - 1, Degree of polynomial,  which is the highest power of the variable in polynomial
    hatA = A.copy()   # hatA = NTT(A)

    v = int(math.log2(n))

    for i in range(v):
        for j in range(2**i):
            # y = Y_table[i + j + 1]
            for k in range(n // 2**(i+1)):
                a_idx = j * n // (2 ** (i)) + k
                jump = n // (2 ** (i + 1))
                
                y = Y_table[i + j + 1]
                print(y)
                # print(i + j + 1)

                at_temp = (hatA[a_idx + jump] * y) % q      # will use barrett soon

                hatA[a_idx + jump] = (hatA[a_idx] - at_temp) % q
                hatA[a_idx] = (hatA[a_idx] + at_temp) % q

    # hatA = indexReverse(hatA, v)
    return hatA

# Example usage
a = [1, 2, 3, 4]
psi = [1, 1925, 3383, 6468]  # Replace with your actual rev-psi array
# q = 9007199379521537
q = 7681
# NTT(a, psi, q)

result = NTT(a, psi, q)
print(result)

