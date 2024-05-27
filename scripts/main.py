from ntt import *
import time
from RNS import *

f = open("data.txt", "r")
# print(f.read().split(" ")[65535])
a = [int(x) for x in f.read().split()]

print("len a", len(a))

# a = a[0:2048]

# Example usage NTT
# a = [5, 6, 7, 8]
# a = [123456, 7891011, 121314, 151617, 123456, 7891011, 121314, 151617, 123456, 7891011, 121314, 151617, 123456, 7891011, 121314, 151617]
psi = 753779
q = 4294828033
# mu = 2251799813689464



psiTable = psi_table(psi, len(a), q)
# print(psiTable)

start_time = time.time()
result = NTT(a, indexReverse(psiTable, int(math.log2(len(psiTable)))), q)
end_time = time.time()

# computation_time_seconds = end_time - start_time
# computation_time_milliseconds = computation_time_seconds * 1e6

# print("Result:", result)
# print("Computation Time:", computation_time_milliseconds, "microsecond")


# print(result)

# Check NTT
# print("")
# print("-------- Sanity check for NTT operations --------")
# if result == expected_hatA:
#     print("Sanity check passed. Result is as expected.")
# else:
#     print("Sanity check failed. Result is not as expected.")
#     print("Expected:", expected_hatA)
#     print("Actual:", result)


# check egcd
# print(mod_inv(42,73))

# for i in range(8):
#     print(bit_reverse(i, 12))

