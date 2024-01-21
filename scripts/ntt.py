# Resource: 

import math
from helper import *

# --- NTT functions ---

# Iterative NTT (Forward and Inverse)
# arrayIn = input polynomial
# P = modulus
# Y = 2nth root of unity (psi)
# inv = 0: forward NTT / 1: inverse NTT
# Input: Standard order/Output: Standard order

def NTT(A, Y_table, q):
    '''
    We refer to negacyclic convolution
    A : Polynomial in coefficient form
    q : Modulus
    Y_table : contains TF (2nth root of unity) constants in bit-reverse, 
    '''
    n = len(A)              # n - 1, Degree of polynomial,  which is the highest power of the variable in polynomial
    hatA = [x for x in A]   # hatA = NTT(A)

    v = int(math.log2(n))
    print('v', v)

    for i in range(v):
        for j in range(2 ** i):
            for k in range(2 ** (v - i - 1)):
                s = j * (2 ** (v - i)) + k
                t = s + (2 ** (v - i - 1))

                y = Y_table[((2 ** i) * k) % n]
                print(y)

                as_temp = hatA[s]
                at_temp = hatA[t]

                hatA[s] = (as_temp + at_temp) % q
                hatA[t] = ((as_temp - at_temp) * y) % q

    hatA = indexReverse(hatA, v)
    return hatA