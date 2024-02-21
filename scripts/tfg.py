from sympy.ntheory.residue_ntheory import nthroot_mod

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
print(nthroot_mod(-1,4,281474976710129)) # for finding y