# Resource: 
# https://doi.org/10.1145/3373376.3378523
# https://eprint.iacr.org/2016/504.pdf

import math
from helper import *

# --- NTT functions ---
def NTT(A, Y_table, q):
    '''
    Iterative Radix-2 Cooley-Tukey Number Theoretic Transform (NTT)
    We refer to negacyclic convolution
    A : Polynomial in coefficient form
    q : Modulus
    Y_table : contains TF (2nth root of unity) constants in bit-reverse order, 
    '''
    n = len(A)        # n - 1, Degree of polynomial,  which is the highest power of the variable in polynomial
    hatA = A.copy()   # hatA = NTT(A)

    v = math.floor(math.log2(n))    # number of stages

    for i in range(v):
        for j in range(2**i):
            # y = Y_table[i + j + 1]
            for k in range(n // 2**(i+1)):
                a_idx = j * n // (2 ** (i)) + k
                jump = n // (2 ** (i + 1))
                # print(a_idx)
                # print(a_idx + jump)
                
                y = Y_table[i + j + 1]
                # print(i + j + 1)
                print(y)

                at_temp = (hatA[a_idx + jump] * y) % q      # will use barrett soon and karatsuba

                hatA[a_idx + jump] = (hatA[a_idx] - at_temp) % q
                hatA[a_idx] = (hatA[a_idx] + at_temp) % q

    hatA = indexReverse(hatA, v)
    return hatA

# --- iNTT functions ---
def iNTT(hatA, Y_table, q):
    '''
    iterative_radix2_gs_intt
    We refer to negacyclic convolution
    hatA : NTT form of A
    q    : Modulus
    Y_table : contains inverse TF (2nth root of unity) constants in bit-reverse, 
    '''
    n = len(hatA)           # n - 1, Degree of polynomial,  which is the highest power of the variable in polynomial
    a = [x for x in hatA]   # A = iNTT(hatA)

    v = int(math.log2(n))   # number of stages

    t = 1
    m = n       # we need value of n for finding the modinv of lenght of polynomial
    # for i in range(v, 0, -1):
    #     j1 = 0
    #     print(i)
    #     for j in range(i):
    #         # print(j1)
    #         # print(j)
    #         for k in range(j1, j1 + t):
    #             a_idx = k
    #             jump = (2 ** (v - i + 2)) // n
    #             # print(jump)
    #             # a_idx = j * n // (2 ** (i)) + k
    #             # jump = n // (2 ** (i + 1))
    #             # print(a_idx)
    #             # print(a_idx + jump)

    #             y = Y_table[j + i]

    #             U = A[a_idx]
    #             V = A[a_idx + t]
    #             A[a_idx] = (U + V) % q
    #             A[a_idx + t] = ((U - V) * y)  % q       # will use barrett soon and karatsuba

    #         j1 = j1 + 2 * t
    #     t = 2 * t
    #     m = m // 2

    while m > 1:
        j1 = 0
        h = m // 2
        for i in range(h):
            j2 = j1 + t - 1
            S = Y_table[h + i]
            for j in range(j1, j2 + 1):
                # print(j)
                # print(j + t)
                # print(h+i)
                # print(S)
                U = a[j]
                V = a[j + t]
                a[j] = (U + V) % q
                a[j + t] = ((U - V) * S) % q
            j1 = j1 + 2 * t
        t = 2 * t
        m = m // 2

    # for m in range(n):
    #     h = m // 2
    #     j1 = 0

    #     for i in range(h):
    #         j2 = j1 + t - 1
    #         S = Y_table[h + i]

    #         for j in range(j1, j2 + 1):
    #             U = a[j]
    #             V = a[j + t]
    #             a[j] = (U + V) % q
    #             a[j + t] = ((U - V) * S) % q

    #         j1 += 2 * t
    #     t *= 2

    inverse_n = modinv(n, q)
    a = [(x*inverse_n) % q for x in a]
    return a



# Example usage NTT
a = [1, 2, 3, 4, 5, 6, 7, 8]
# a = [1, 2, 3, 4]
psi = [1, 1925, 3383, 6468, 7680, 5756, 4298, 1213]  # Replace with your actual psi array
# q = 9007199379521537
q = 7681

result = NTT(a, indexReverse(psi, int(math.log2(len(psi)))), q)

expected_hatA = [7673, 5349, 976, 1032, 3660, 3813, 3037, 5192]

# Check NTT
print("")
print("-------- Sanity check for NTT operations --------")
if result == expected_hatA:
    print("Sanity check passed. Result is as expected.")
else:
    print("Sanity check failed. Result is not as expected.")
    print("Expected:", expected_hatA)
    print("Actual:", result)


# Example usage iNTT
# hatA = [1467, 2807, 3471, 7621]
hatA = [7673, 5349, 976, 1032, 3660, 3813, 3037, 5192]
inversePsi = [1, 1213, 4298, 5756, 7680, 6468, 3383, 1925]  # Replace with your actual inversePsi array
# inversePsi = [1, 1213, 4298, 5756]
reverse_hatA = indexReverse(hatA , int(math.log2(len(hatA))))
# q = 9007199379521537
q = 7681
# print(indexReverse(inversePsi, int(math.log2(len(inversePsi)))))
# print(reverse_hatA)
result = iNTT(reverse_hatA, indexReverse(inversePsi, int(math.log2(len(inversePsi)))), q)

# a = [1, 2, 3, 4]
a = [1, 2, 3, 4, 5, 6, 7, 8]

# Check iNTT
print("")
print("-------- Sanity check for iNTT operations -------")
if result == a:
    print("Sanity check passed. Result is as expected.")
else:
    print("Sanity check failed. Result is not as expected.")
    print("Expected:", a)
    print("Actual:", result)
