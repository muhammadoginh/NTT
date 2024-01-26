def indexReverse(B, v):
    '''
    B : NTT result in bit-reverse order (BO)
    '''
    n = len(B)
    reversed_indices = [0] * n

    for i in range(n):
        reversed_indices[i] = int(format(i, '0' + str(v) + 'b')[::-1], 2)

    result = [0] * n
    for i in range(n):
        result[reversed_indices[i]] = B[i]

    return result

# # Example usage
# B = [0, 1, 2, 3]
# v = 2

# reversed_B = indexReverse(B, v)
# print(reversed_B)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def generate_Y_table(n, q):
    Y_table = [1]  # Start with the first element, which is 1 (2^0 mod q)

    primitive_root = 2  # A common choice for a primitive root

    for i in range(1, n):
        next_element = pow(primitive_root, (q - 1) // (2**i), q)
        Y_table.append(next_element)

    return Y_table[::-1]  # Return the list in bit-reversed order

# # Example usage
# n = 4  # Adjust as needed
# q = 7681  # Adjust as needed
# Y_table = generate_Y_table(n, q)
# print(Y_table)


# def find_primitive_root(n, q):
#     # Find a primitive root by brute force
#     for i in range(2, q):
#         if pow(i, n, q) == 1:
#             return i

# # Example usage
# n = 4  # Size of the input array
# q = 7681  # Chosen prime modulus

# Y_table = generate_Y_table(n, q)
# print(Y_table)
        