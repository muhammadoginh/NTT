# Resource: 
# https://doi.org/10.1145/3373376.3378523
# https://eprint.iacr.org/2016/504.pdf
# iNTT: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9114594

import math
from helper import *
import csv

# Cooley-Tukey Butterfly Structure
# A0,A1: input coefficients
# W: twiddle factor
# q: modulus
# B0,B1: output coefficients
def CT_Butterfly(A0,A1,W,q):
    """
    A0 -------\--|+|-- B0
               \/
               /\
    A1 --|x|--/--|-|-- B1
    """
    M = (A1 * W) % q

    B0 = (A0 + M) % q
    B1 = (A0 - M) % q

    return B0,B1

# Gentleman-Sandle Butterfly Structure
# A0,A1: input coefficients
# W: twiddle factor
# q: modulus
# B0,B1: output coefficients
def GS_Butterfly(A0,A1,W,q):
    """
    A0 --\--|+|------- B0
          \/
          /\
    A1 --/--|-|--|x|-- B1
    """
    M0 = (A0 + A1) % q
    M1 = (A0 - A1) % q

    B0 = M0
    B1 = (M1 * W) % q

    return B0,B1

def DIV2(n,q):
    if (n % 2 == 0):
        n = n >> 1
    else: # n is odd
        n = (n >> 1) + ((q + 1) >> 1)
    return n

def GS_BU_DIV2(A0,A1,W,q):
    """
    A0 --\--|+|------- B0
          \/
          /\
    A1 --/--|-|--|x|-- B1
    """
    M0 = (A0 + A1) % q
    M1 = (A0 - A1) % q

    B0 = M0
    B1 = (M1 * W) % q

    return DIV2(B0,q),DIV2(B1,q)

# --- PSI Table ---
# def psi_table(psi, n, q):
#     print("================== Start PSI ======================")
#     psi_table = []
#     for i in range(n):
#         psi_table.append((psi**i) % q)
#         print("get psi", i)
#     return psi_table

# def psi_table(psi, n, q):
#     psi_table = [0] * n
#     # Initialize the first value in the table
#     psi_table[0] = (psi ** 0) % q

#     # Compute the remaining values in the table using the previous value
#     for i in range(1, n):
#         psi_table[i] = (psi_table[i-1] * psi) % q
#         print("get psi", i)

#     return psi_table

def psi_table(psi, n, q):
    """
    Dynamic programming implementation
    """
    psi_table = [0] * n
    psi_table[0] = 1
    for i in range(1, n):
        psi_table[i] = (psi * psi_table[i-1]) % q
        # print("get psi", i)
    return psi_table

# --- NTT functions ---
def NTT(A, Y_table, q):
    '''
    Iterative Radix-2 Cooley-Tukey Number Theoretic Transform (NTT)
    We refer to negacyclic convolution
    A : Polynomial in coefficient form
    q : Modulus
    Y_table : contains TF (2nth root of unity) constants in bit-reverse order, 
    hatA : bit-reverse order 
    '''
    n = len(A)        # n - 1, Degree of polynomial,  which is the highest power of the variable in polynomial
    hatA = A.copy()   # hatA = NTT(A)

    v = math.floor(math.log2(n))    # number of stages

    t = n >> 1
    m = 1  
    # print(n)     

    print("NTT ... ")
    print("")

    header_row = ['Stage {}'.format(i) for i in range(1, v + 1)]
    rows_data = []  # To store data for each step in each stage # for save coeff_idx
  
    while m < n:
        # print("stage", v)  # number of stage log(n)
        # print(hatA)
        stage_data = []  # To store data for each step in this stage # for save coeff_idx
        for i in range(m):
            idx_omega = m + i
            y = Y_table[idx_omega]
            for a_idx in range(i * 2**v, (i * 2**v) + t):
                # n_bu = n_bu + 1
                
                # print(a_idx, a_idx + t)
                # print(bit_reverse(idx_omega, 4))
                # f = open("idx.txt", "a")
                # f.write(str(bit_reverse(idx_omega, 16)))
                # f.write(str(a_idx))
                # f.write("\n")
                # f.close()  
                # print(bit_reverse(idx_omega, 4))
                # print(y)
                # print(a_idx, a_idx + t)

                stage_data.append(y)

                # stage_data.append(bit_reverse(idx_omega, 12)) # for save omega_idx

                # stage_data.append(a_idx)        # for save coeff_idx
                # stage_data.append(a_idx + t)    # for save coeff_idx

                # print(a_idx)  # number of BU for each stage n/2
                hatA[a_idx], hatA[a_idx + t] = CT_Butterfly(hatA[a_idx], hatA[a_idx + t], y, q)
        # print(hatA)
        # print("number of BU", n_bu)
        # data.append(row_data)
        rows_data.append(stage_data)  # Append data for this stage # for save coeff_idx
        v -= 1
        t = t//2
        m = m*2
    # hatA = indexReverse(hatA, v)  # uncomment to get normal order

    # for save coeff_idx
    # with open('coeff_idx.csv', 'w', newline='\n') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(header_row)  # Write header row
    #     writer.writerows(zip(*rows_data))  # Write transposed rows data (each row represents a step in each stage)
        
    # for save omega_idx
    # with open('omega_idx.csv', 'w', newline='\n') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(header_row)  # Write header row
    #     writer.writerows(zip(*rows_data))  # Write transposed rows data (each row represents a step in each stage)

    # for save omega
    # with open('omega.csv', 'w', newline='\n') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(header_row)  # Write header row
    #     writer.writerows(zip(*rows_data))  # Write transposed rows data (each row represents a step in each stage)
    return hatA


# --- iNTT functions ---
def iNTT(hatA, Y_table, q):
    '''
    iterative_radix2_gs_intt GS_Butterfly
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

    while m > 1:
        j1 = 0
        h = m // 2
        print("########### Stage", int(math.log2(n//m)) + 1, "###########")
        for i in range(h):
            j2 = j1 + t - 1
            S = Y_table[h + i]
            
            for j in range(j1, j2 + 1):
                print(bit_reverse(h + i, 4))
                print(S)
                print(j, j + t)

                a[j], a[j + t] = GS_Butterfly(a[j], a[j + t], S, q)

            j1 = j1 + 2 * t
        t = 2 * t
        m = m // 2
        print(a)


    inverse_n = modinv(n, q)
    a = [(x*inverse_n) % q for x in a]
    return a

def iNTT_modified(hatA, Y_table, q):
    '''
    iterative_radix2_gs_intt GS_Butterfly with DIV2
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

    while m > 1:
        j1 = 0
        h = m // 2
        print("########### Stage", int(math.log2(n//m)) + 1, "###########")
        for i in range(h):
            j2 = j1 + t - 1
            S = Y_table[h + i]
            
            for j in range(j1, j2 + 1):
                print(bit_reverse(h + i, 4))
                print(S)
                print(j, j + t)

                a[j], a[j + t] = GS_BU_DIV2(a[j], a[j + t], S, q)

            j1 = j1 + 2 * t
        t = 2 * t
        m = m // 2
        print(a)

    return a


################ start uncomment for sanitycheck #################
# # Example usage NTT
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# psi = [1, 97, 1728, 6315, 5756, 5300, 7154, 2648, 3383, 5549, 583, 2784, 1213, 2446, 6832, 2138]  # Replace with your actual psi array
# # q = 9007199379521537
# q = 7681


# result = NTT(a, indexReverse(psi, int(math.log2(len(psi)))), q)

# # expected_hatA = [1467, 2807, 3471, 7621]  # after indexReverse
# expected_hatA = [1467, 3471, 2807, 7621]

# # Check NTT
# print("")
# print("-------- Sanity check for NTT operations --------")
# if result == expected_hatA:
#     print("Sanity check passed. Result is as expected.")
# else:
#     print("Sanity check failed. Result is not as expected.")
#     print("Expected:", expected_hatA)
#     print("Actual:", result)


# # Example usage iNTT
# hatA = [1467, 2807, 3471, 7621]
# # hatA = [7673, 5349, 976, 1032]
# inversePsi = [1, 1213, 4298, 5756]  # Replace with your actual inversePsi array
# # inversePsi = [1, 1213, 4298, 5756]
# reverse_hatA = indexReverse(hatA , int(math.log2(len(hatA))))
# # q = 9007199379521537
# q = 7681
# # print(indexReverse(inversePsi, int(math.log2(len(inversePsi)))))
# # print(reverse_hatA)
# result = iNTT(reverse_hatA, indexReverse(inversePsi, int(math.log2(len(inversePsi)))), q)

# # a = [1, 2, 3, 4]
# a = [1, 2, 3, 4]

# # Check iNTT
# print("")
# print("-------- Sanity check for iNTT operations -------")
# if result == a:
#     print("Sanity check passed. Result is as expected.")
# else:
#     print("Sanity check failed. Result is not as expected.")
#     print("Expected:", a)
#     print("Actual:", result)
################ end uncomment for sanitycheck ###################