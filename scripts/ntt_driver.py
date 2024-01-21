from ntt import *


# Example usage
A = [5, 6, 7, 8]
Y_table = [1, 3383, 7680, 4298]  # Replace with your actual W_table values
q = 7681

result = NTT(A, Y_table, q)
print(result)