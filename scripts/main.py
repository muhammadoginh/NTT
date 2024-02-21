from ntt import *

# Example usage NTT
# a = [5, 6, 7, 8]
a = [123456, 7891011, 121314, 151617]
psi = 12967992388
q = 281474976710129
mu = 2251799813689464

psiTable = psi_table(psi, 4, q)
print(psiTable)

result = NTT(a, indexReverse(psiTable, int(math.log2(len(psiTable)))), q)

print(result)

# Check NTT
# print("")
# print("-------- Sanity check for NTT operations --------")
# if result == expected_hatA:
#     print("Sanity check passed. Result is as expected.")
# else:
#     print("Sanity check failed. Result is not as expected.")
#     print("Expected:", expected_hatA)
#     print("Actual:", result)
