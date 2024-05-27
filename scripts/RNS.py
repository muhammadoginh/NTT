def mod_inv(a, b):
    """
    a : input value
    b : modulus
    """
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1



def gcd(a, b):
    while (a != b):
        if (a > b):
            a = a - b
        else:
            b = b - a
        print(f"nilai a: {a}, nilai b: {b}")
    return b

def multiply(moduli):
    prod = 1
    for i in moduli:
        prod = prod*i
    return prod

def CRT(moduli, remainder):
    '''
    First method
    '''
    sum = 0
    prod = multiply(moduli)
    for n_i, a_i in zip(moduli, remainder):
        p = prod // n_i
        sum += a_i * mod_inv(p, n_i) * p
        # print(a_i, mod_inv(p, n_i), p)
        # print(sum)
    return sum % prod

def CRT_V2(moduli, remainder):
    '''
    Second method
    '''
    sum = 0
    prod = multiply(moduli)
    for n_i, a_i in zip(moduli, remainder):
        p = prod // n_i
        sum += (a_i * mod_inv(p, n_i) % n_i) * p
    return sum % prod

def RNS_Conv(moduli, remainder):
    '''
    another name for CRT
    '''
    sum = 0
    prod = multiply(moduli)
    for n_i, a_i in zip(moduli, remainder):
        p = prod // n_i
        sum += a_i * mod_inv(p, n_i) * p
    return sum % prod

def v(moduli, remainder):
    sum = 0
    prod = multiply(moduli)
    for n_i, a_i in zip(moduli, remainder):
        p = prod // n_i
        sum += (a_i * mod_inv(p, n_i) % n_i) / n_i
    return int(sum)

def BaseExtend(moduli, remainder, moduli_p):
    sum = 0
    q = multiply(moduli)
    for q_i, x_i in zip(moduli, remainder):
        q_star_i = q // q_i
        sum += (x_i * mod_inv(q_star_i, q_i) % q_i) * (q_star_i % moduli_p)
    x_j = sum - v(moduli, remainder)*(q % moduli_p)
    return x_j % moduli_p

def u(moduli, remainder, moduli_p):
    sum = 0
    q = multiply(moduli)
    p = multiply(moduli_p)
    for x_i, q_i in zip(remainder, moduli):
        q_star_i = q // q_i
        sum += ((x_i * mod_inv(q_star_i, q_i) * p) % q_i) / q_i
    return int(sum)

def ModSwitch(moduli, remainder, moduli_p):
    sum = 0
    q = multiply(moduli)
    p = multiply(moduli_p)
    for x_i, q_i in zip(remainder, moduli):
        q_star_i = q // q_i
        sum += ((x_i * mod_inv(q_star_i, q_i) * p) % q_i) * mod_inv(q_i, moduli_p[0])
    return (u(moduli, remainder, moduli_p) - sum) % moduli_p[0]

def ScaleDown(moduli, remainder, remainder_p, moduli_p, t):
    sum = 0
    q = multiply(moduli)
    p = multiply(moduli_p)

    for x_j, p_j in zip(remainder_p, moduli_p):
        p_star_j = p // p_j
        Q_tilde_j = mod_inv(q*p_star_j/moduli[0], p_j)
        sum += (x_j * (t*q*Q_tilde_j/p_j))

    Q_tilde_i = mod_inv(p*q/moduli[0], moduli[0])

    return (int(sum) + remainder[0]*((t*Q_tilde_i*q/moduli[0]) % moduli[0])) % moduli[0]

def FastBaseExtention(remainder, moduli_Q, moduli_p):
    sum = 0
    Q = multiply(moduli_Q)
    for q_i, x_i in zip(moduli_Q, remainder):
        q_star_i = Q // q_i
        sum += (x_i * mod_inv(q_star_i, q_i) % q_i) * q_star_i
    return sum % moduli_p




# moduli = []
# remainder = []
# n = int(input("How many moduli: "))
# for i in range(n):
#     x = int(input(f"Moduli {i+1}: "))
#     y = int(input(f"Remainder {i+1}: "))
#     moduli.append(x)
#     remainder.append(y)


# for Q
# moduli = [281474976694273, 281474976546817, 102855858655377]
# remainder = [73044306017135, 70674865281097, 275473514777291]

# for P
# moduli = [281474975662081, 281474975563777, 281474975367169, 281474975285249]
# remainder = [73044306017135, 70674865281097, 275473514777291]

# Original HPS BFV
# moduli = [281474976694273, 281474976546817, 281474976317441, 281474975662081, 281474975563777, 281474975367169, 281474975285249]
# remainder = [196093176550158, 189642359124622, 166661595510124, 9185168279998, 277399166238365, 171946455059814, 102276390093506]
# moduli_p = 281474975662081

# HPSPOVERQ BFV
# moduli = [281474976694273, 281474976546817, 281474976317441, 281474975662081, 281474975563777, 281474975367169]
# remainder = [232982797791481, 84337766426150, 207961317167224, 79653720283223, 45197324822525, 250002149798656]
# 240889960524428, 148794893243363, 205665602644360
# moduli = [281474976694273, 281474976546817, 281474976317441]
# remainder = [232982797791481, 84337766426150, 207961317167224]
moduli = [4294828033, 4294729729, 4294483969]
remainder = [3574136608, 981484964, 1765082793]
moduli_p = [4294475777, 4294451201, 4294008833]
remainder_p = [1695292834, 1606737724, 3736971249]

t = 65537


residu = CRT(moduli, remainder)

baseExtend = BaseExtend(moduli, remainder, moduli_p[0])

modSwitch = ModSwitch(moduli, remainder, moduli_p)

scaleDown = ScaleDown(moduli, remainder, remainder_p, moduli_p, t)

fastBaseExtention = FastBaseExtention(remainder, moduli, moduli_p[0])

print("The value of modulo in CRT is", residu)
print("The value of BaseExtend BFV", baseExtend)
print("The value of ModSwitch BFV", modSwitch)
print("The value of ScaleDown BFV", scaleDown)
print("The value of FastBaseExtention BFV", fastBaseExtention)

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

# print(mod_inv(15,105))

# print(gcd(113939870916378, 11113050027888))
# print(gcd(110238117147976, 57250409645146))
# print(gcd(27, 24))

def mod_inverse(a, b):
    t = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += t
    return x1

# Example usage:
a = 753779
b = 4294828033
result = mod_inverse(a, b)
print("Modular Inverse of", a, "mod", b, ":", result)