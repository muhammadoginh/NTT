# Resource: https://ieeexplore.ieee.org/document/4272869

import math
import time

def Folding_Barrett_Reduction(X, P):

    # pre-computation
    # Assume k = 2s
    k = math.ceil(math.log2(P))
    s = k/2
    mu = pow(2, 3*s) // P
    P0 = pow(2, 3*s) % P

    # Barrett Reduction
    q1 = X // pow(2, 3*s)
    q2 = q1 * P0
    X0 = (X % pow(2, 3 * s)) + q2
    q3 = X0 // pow(2, 2*s)
    q4 = q3 * mu
    q5 = q4 // pow(2, s)
    r1 = (X0 % pow(2, 2 * s + 2)) - (q5 * P % pow(2, 2 * s + 2))
    r2 = r1 - P
    r3 = r1 - 2 * P
    r4 = r1 - 3 * P
    
    # Choose {r ∈ {r1, r2, r3, r4} | 0 ≤ r < P}
    if 0 <= r1 < P:
        return r1
    elif 0 <= r2 < P:
        return r2
    elif 0 <= r3 < P:
        return r3
    else:
        return r4

# Example usage
# X = 1467 * 2489
# P = 7681

# result = Folding_Barrett_Reduction(X, P)
# print("Result:", result)


# Test case 1
X = 1467 * 2489
P = 7681

# Measure computation time
start_time = time.time()
result = Folding_Barrett_Reduction(X, P)
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
result = Folding_Barrett_Reduction(X, P)
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
result = Folding_Barrett_Reduction(X, P)
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
result = Folding_Barrett_Reduction(X, P)
end_time = time.time()

computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6

print("Result:", result)
print("Computation Time:", computation_time_milliseconds, "microsecond")