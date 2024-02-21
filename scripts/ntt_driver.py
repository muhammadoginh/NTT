from ntt import *


# Example usage
A = [1, 2, 3, 4]
Y_table = [1, 78055169708279, 281474976710128, 203419807001850]  # Replace with your actual W_table values
q = 281474976710129

result = NTT(A, indexReverse(Y_table, int(math.log2(len(Y_table)))), q)
print(result)

A = [5, 6, 7, 8]
Y_table = [1, 78055169708279, 281474976710128, 203419807001850]  # Replace with your actual W_table values
q = 281474976710129

result = NTT(A, indexReverse(Y_table, int(math.log2(len(Y_table)))), q)
print(result)