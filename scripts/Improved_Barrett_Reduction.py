# Resource: https://ieeexplore.ieee.org/document/5676912

import math
import time

def Improved_Barrett_Reduction(X, P):

    # pre-computation
    k = math.ceil(math.log2(P))
    mu = 2**(2*k + 3) // P

    # Barrett Reduction
    q1 = X // 2**(k - 2)
    q2 = q1 * mu
    q3 = q2 // 2**(k + 5)
    r1 = X % (2**(k+1)) - (q3*P % (2**(k+1)))
    r2 = r1 - P
    # choose {r ∈ {r1, r2}|0 ≤ r < P}
    if 0 <= r1 < P:
        r = r1
    else:
        r = r2

    return(r)

# Test case 1
X = 1467 * 2489
P = 7681

# Measure computation time
start_time = time.time()
result = Improved_Barrett_Reduction(X, P)
end_time = time.time()

computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6

print("Result:", result)
print("Computation Time:", computation_time_milliseconds, "microsecond")

# Test case 2
X = 1467 * 2489
P = 10681

# Measure computation time
start_time = time.time()
result = Improved_Barrett_Reduction(X, P)
end_time = time.time()

computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6

print("Result:", result)
print("Computation Time:", computation_time_milliseconds, "microsecond")

# Test case 3
X = 1467 * 2489
P = 17681

# Measure computation time
start_time = time.time()
result = Improved_Barrett_Reduction(X, P)
end_time = time.time()

computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6

print("Result:", result)
print("Computation Time:", computation_time_milliseconds, "microsecond")

# Test case 4
X = 1467 * 2489
P = 56811

# Measure computation time
start_time = time.time()
result = Improved_Barrett_Reduction(X, P)
end_time = time.time()

computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6

print("Result:", result)
print("Computation Time:", computation_time_milliseconds, "microsecond")