from sympy.ntheory.residue_ntheory import nthroot_mod
from helper import *

q = [
    281474976710129,
    140737488356329,
    140737488353633,
    140737488356321,
    140737488353713,
    140737488356281,
    140737488353809,
    140737488356209,
    140737488353849,
    140737488356177,
    140737488354041,
    140737488356009,
    140737488354161,
    140737488355609,
    140737488354233,
    140737488355601,
    140737488354329,
    140737488355441,
    140737488354409,
    140737488355393,
    140737488355049,
    140737488355369,
    140737488355201,
    140737488355337,
    281474976710089,
    281474976709649,
    281474976709609,
    281474976709361,
    281474976709273,
    281474976709249
]

# find the 2n-th root of unity

x = 1
n = 2

# check the existing of 2n-th root of unity for each given moduli
# for i in q:
#     if (x == i % (2*n)):
#         print("there exist 2n-th root of unity for index", i)
#     else:
#         print("there is not exist 2n-th root of unity")


# sympy.ntheory.residue_ntheory.nthroot_mod(a, n, p, all_roots=False)
# Find the solutions to x**n = a mod p.

# for i in q:
#     print(nthroot_mod(-1, 2, i))

# print(nthroot_mod(1,4,192394209554001)) # for finding w
# print(nthroot_mod(-1,65536,281474976317441)) # for finding y
# print(nthroot_mod(-1,8,281474976710129))

def tfg(n, q):
    psi = int(nthroot_mod(-1,n,q))
    print("Still writing to table...")
    Y_table = []  # Start with the first element, which is 1 (psi^0 mod q)
    memo = 1
    
    for i in range(n):
        if i == 0:
            next_element = memo
        else:
            next_element = (memo*psi) % q
            memo = next_element
            # print(memo)
        Y_table.append(next_element)

    # Convert the list to a string with each element on a separate line
    result_str = '\n'.join(map(str, Y_table))
        # result_str = ''.join(map(str, Y_table))
    return Y_table
    # return result_str

# n = 16
# q = 281474976317441

# n = 8
# q = 281474976710129

# n = 4
# q = 281474976710129

# n = 16
# q = 281474976709249


# n = 2**16
# q = 281474976317441


# BFV 
# n = 8192
# q = 281474976694273

n = 4096
q = 4294828033


result = tfg(16, 4294828033)
# print(result)



# Write the result to a file
# output_filename = "psitable.mem"
# with open(output_filename, 'w') as output_file:
#     for number in result:
#         output_file.write(hex(number)[2:] + '\n')

# modinv
output_filename = "inv_psitable_16.mem"
with open(output_filename, 'w') as output_file:
    for number in result:
        output_file.write(hex(modinv(number, q))[2:] + '\n')

print("Finish")
# print(tfg(8,673)) 

# print("modulus q")
# print("1073692673",nthroot_mod(-1,4096,1073692673))
# print("1073668097",nthroot_mod(-1,4096,1073668097))
# print("1073651713",nthroot_mod(-1,4096,1073651713))

# print("modulus p")
# print("1073643521",nthroot_mod(-1,4096,1073643521))
# print("1073569793",nthroot_mod(-1,4096,1073569793))
# print("1073479681",nthroot_mod(-1,4096,1073479681))

