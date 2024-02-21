# Resource: https://ieeexplore.ieee.org/document/5676912

import math
import time

def Improved_Barrett_Reduction(X, P):

    # pre-computation
    k = math.ceil(math.log2(P))
    mu = 2**(2*k + 3) // P
    print("mu:", mu)

    # Barrett Reduction
    # q1 = X // 2**(k - 2)
    q1 = X >> (k - 2)
    # print("q1:", q1)
    q2 = q1 * mu
    # print("q2:", q2)
    # q3 = q2 // 2**(k + 5)
    q3 = q2 >> (k + 5)
    # print("q3:", q3)
    # r1 = X % (2**(k+1)) - (q3*P % (2**(k+1)))
    r = X - q3*P
    # print("r:", r)
    # choose {r ∈ {r1, r2}|0 ≤ r < P}
    if r > P:
        r = r - P

    return(r)

# Test case 1
X = 31235006325818 * 147300061358300
P = 281474976710129

# Measure computation time
start_time = time.time()
result = Improved_Barrett_Reduction(X, P)
end_time = time.time()

computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6

print("Result:", result)
print("Computation Time:", computation_time_milliseconds, "microsecond")

# Test case 2
X = 263230795212639 * 47918723023213
P = 281474976710129

# Measure computation time
start_time = time.time()
result = Improved_Barrett_Reduction(X, P)
end_time = time.time()

computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6

print("Result:", result)
print("Computation Time:", computation_time_milliseconds, "microsecond")

# Test case 3
X = 136216848817676 * 192751993893431
P = 281474976710129

# Measure computation time
start_time = time.time()
result = Improved_Barrett_Reduction(X, P)
end_time = time.time()

computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6

print("Result:", result)
print("Computation Time:", computation_time_milliseconds, "microsecond")

# Test case 4
X = 89084525283856 * 178054022353922
P = 281474976710129

# Measure computation time
start_time = time.time()
result = Improved_Barrett_Reduction(X, P)
end_time = time.time()

computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6

print("Result:", result)
print("Computation Time:", computation_time_milliseconds, "microsecond")