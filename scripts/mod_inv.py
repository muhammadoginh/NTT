def modular_inverse_with_barrett_reduction(a, b):
    # Compute Barrett Reduction Constants
    k = b.bit_length()  # Number of bits in the binary representation of b
    mu = 2**(2*k) // b

    # Perform Barrett Reduction
    q = a >> (k - 1)
    r = a - q * b
    if r >= b:
        r -= b

    # Use Barrett Reduction to find modular inverse
    x = (mu * (1 << (2*k))) % b
    for _ in range(k):
        x = x * (2 - b * x) % b

    # Return modular inverse if it exists
    if r == 1:
        return x
    else:
        return None  # Modular inverse does not exist

# Example usage
a = 42
b = 73
mod_inv = modular_inverse_with_barrett_reduction(a, b)
print("Modular inverse of", a, "modulo", b, "is:", mod_inv)
