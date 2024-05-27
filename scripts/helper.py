# Bit-Reverse integer
def bit_reverse(a, n):
    return int(('{:0'+str(n)+'b}').format(a)[::-1],2)

def indexReverse(B, v):
    '''
    B : NTT result in bit-reverse order (BO)
    '''
    n = len(B)
    reversed_indices = [0] * n

    for i in range(n):
        reversed_indices[i] = bit_reverse(i, v) # int(format(i, '0' + str(v) + 'b')[::-1], 2)

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


# Check if input is m-th (could be n or 2n) primitive root of unity of q
def isrootofunity(w,m,q):
    if pow(w,m,q) != 1:
        return False
    elif pow(w,m//2,q) != (q-1):
        return False
    else:
        v = w
        for i in range(1,m):
            if v == 1:
                return False
            else:
                v = (v*w) % q
        return True


# # Example usage
# n = 4  # Size of the input array
# q = 7681  # Chosen prime modulus

# Y_table = generate_Y_table(n, q)
# print(Y_table)
        

def read_2d_data(file_path):
    """
    This function return integer of 2 dimension data
    """
    try:
        with open(file_path, 'r') as file:
            # Read each line and split the integers
            lines = file.readlines()
            integer_array_2d = [list(map(int, line.split())) for line in lines]
            return integer_array_2d
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
        
def read_1d_data(file_path):
    """
    This function return integer of 1 dimension data
    """
    try:
        with open(file_path, 'r') as file:
            # All value are stored as space-separated values in the file
            integer_array = [int(num) for num in file.read().split()]
            return integer_array
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
