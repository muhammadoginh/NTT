def mod_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def multiply(moduli):
    prod = 1
    for i in moduli:
        prod = prod*i
    return prod

def CRT(moduli, remainder):
    sum = 0
    prod = multiply(moduli)
    for n_i, a_i in zip(moduli, remainder):
        p = prod // n_i
        sum += a_i * mod_inv(p, n_i) * p
    return sum % prod

def RNS_Conv(moduli, remainder):
    sum = 0
    prod = multiply(moduli)
    for n_i, a_i in zip(moduli, remainder):
        p = prod // n_i
        sum += a_i * mod_inv(p, n_i) * p
    return sum % prod

# moduli = []
# remainder = []
# n = int(input("How many moduli: "))
# for i in range(n):
#     x = int(input(f"Moduli {i+1}: "))
#     y = int(input(f"Remainder {i+1}: "))
#     moduli.append(x)
#     remainder.append(y)

# residu = CRT(moduli, remainder)

# print("The value of modulo in CRT is", residu)

# print(mul_inv(129, 6841))

# test = [281474976710129,
# 140737488353401,
# 140737488356537,
# 140737488353569,
# 140737488356329,
# 140737488353633,
# 140737488356321,
# 140737488353713,
# 140737488356281,
# 140737488353809,
# 140737488356209,
# 140737488353849,
# 140737488356177,
# 140737488354041,
# 140737488356009,
# 140737488354161,
# 140737488355609,
# 140737488354233,
# 140737488355601,
# 140737488354329,
# 140737488355441,
# 140737488354409,
# 140737488355393,
# 140737488355049,
# 140737488355369,
# 140737488355201,
# 140737488355337,
# 281474976710089,
# 281474976709649,
# 281474976709609,
# ]

# print(multiply(test))