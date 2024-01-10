# Resource: https://dx.doi.org/10.1007/3-540-47721-7_24

import math
import time

def General_Barrett_Reduction(X, P):

    # pre-computation
    k = math.ceil(math.log2(P))
    mu = 2**(2*k) // P

    # Barrett Reduction
    q1 = X // 2**k
    q2 = q1 * mu
    q3 = q2 // 2**k
    r1 = X % (2**(k+2)) - (q3*P % (2**(k+2)))
    r2 = r1 - P
    r3 = r1 - 2*P
    # choose {r ∈ {r1, r2, r3}|0 ≤ r < P}
    if 0 <= r1 < P:
        r = r1
    elif 0 <= r2 < P:
        r = r2
    else:
        r = r3

    return(r)

# Test case 1
X = 1467 * 2489
P = 7681

# Measure computation time
start_time = time.time()
result = General_Barrett_Reduction(X, P)
end_time = time.time()

computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6

print("Result:", result)
print("Computation Time:", computation_time_milliseconds, "microsecond")

# # Test case 2
# X = 1467 * 2489
# P = 10681

# # Measure computation time
# start_time = time.time()
# result = General_Barrett_Reduction(X, P)
# end_time = time.time()

# computation_time_seconds = end_time - start_time
# computation_time_milliseconds = computation_time_seconds * 1e6

# print("Result:", result)
# print("Computation Time:", computation_time_milliseconds, "microsecond")

# # Test case 3
# X = 1467 * 2489
# P = 17681

# # Measure computation time
# start_time = time.time()
# result = General_Barrett_Reduction(X, P)
# end_time = time.time()

# computation_time_seconds = end_time - start_time
# computation_time_milliseconds = computation_time_seconds * 1e6

# print("Result:", result)
# print("Computation Time:", computation_time_milliseconds, "microsecond")

# # Test case 4
# X = 1467 * 2489
# P = 56811

# # Measure computation time
# start_time = time.time()
# result = General_Barrett_Reduction(X, P)
# end_time = time.time()

# computation_time_seconds = end_time - start_time
# computation_time_milliseconds = computation_time_seconds * 1e6

# print("Result:", result)
# print("Computation Time:", computation_time_milliseconds, "microsecond")


### input variaton
# Test case 1
X = 740 * 891 # bit length 20
P = 7681

# Measure computation time
start_time = time.time()
result = General_Barrett_Reduction(X, P)
end_time = time.time()

computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6

print("Result:", result)
print("Computation Time:", computation_time_milliseconds, "microsecond")

# Test case 2
X = 21034 * 20604 # bit length 30
P = 7681

# Measure computation time
start_time = time.time()
result = General_Barrett_Reduction(X, P)
end_time = time.time()

computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6

print("Result:", result)
print("Computation Time:", computation_time_milliseconds, "microsecond")

# Test case 3   # bit length 40
X = 802553 * 835321
P = 7681

# Measure computation time
start_time = time.time()
result = General_Barrett_Reduction(X, P)
end_time = time.time()

computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6

print("Result:", result)
print("Computation Time:", computation_time_milliseconds, "microsecond")

# Test case 4   # bit length 50
X = 26730299 * 28824379
P = 7681

# Measure computation time
start_time = time.time()
result = General_Barrett_Reduction(X, P)
end_time = time.time()

computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6

print("Result:", result)
print("Computation Time:", computation_time_milliseconds, "microsecond")


# Test case 5   # bit length 60
X = 866769074 * 911769074
P = 7681

# Measure computation time
start_time = time.time()
result = General_Barrett_Reduction(X, P)
end_time = time.time()

computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6

print("Result:", result)
print("Computation Time:", computation_time_milliseconds, "microsecond")