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
# B = [1, 2, 3, 4]
# v = 2

# reversed_B = indexReverse(B, v)
# print(reversed_B)

def generate_Y_table(n, q):

    # Calculate the powers of the primitive root
    Y_table = [1] * n
    current_power = 1

    # Find a primitive 2nth root of unity modulo q
    for i in range(2, q):
        if (pow(i, 2, q) == find_primitive_root(n, q)) and (pow(i, n, q) == -1):
           primitive_root = i
           for i in range(1, n):
                current_power = (current_power * primitive_root) % q
                Y_table[i] = current_power

    return Y_table

def find_primitive_root(n, q):
    # Find a primitive root by brute force
    for i in range(2, q):
        if pow(i, n, q) == 1:
            return i

# Example usage
n = 4  # Size of the input array
q = 7681  # Chosen prime modulus

Y_table = generate_Y_table(n, q)
print(Y_table)