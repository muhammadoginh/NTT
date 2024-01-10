# Resource: https://ieeexplore.ieee.org/document/6467863

import math
import time

def Improved_Folding_Barrett_Reduction(A, B, P):
    # Pre-computation
    k = math.ceil(math.log2(P))
    s = k // 2
    mu = pow(2, 3 * s + 3) // P  # Calculate mu using modular exponentiation
    P0 = pow(2, 3 * s) % P  # Calculate P0 using modular exponentiation

    # Split the numbers into halves
    A_L, A_H = A & ((1 << s) - 1), A >> s  # A = A_H * 2^s + A_L
    B_L, B_H = B & ((1 << s) - 1), B >> s  # B = B_H * 2^s + B_L

    # Barrett Reduction
    q1 = (A_H * B_H) >> s  # Step 1: q1 ← (A_H * B_H) // 2^s
    q2 = q1 * P0  # Step 2: q2 ← q1 * P0 mod P
    q3 = pow(2, 2 * s) * (A_H * B_H % (1 << s)) + pow(2, s) * ((A_H + A_L) * (B_H + B_L) - A_H * B_H - A_L * B_L) + A_L * B_L   # Step 3: q3 
    X00 = (q2 + q3)  # Step 4: X00 ← (q2 + q3) mod P
    q4 = X00 >> (2 * s + 2)  # Step 5: q4 ← X00 // 2^(2s+2)
    q5 = q4 * mu  # Step 6: q5 ← q4 * mu mod P
    q6 = q5 >> (s + 5)  # Step 7: q6 ← q5 // 2^(s+5)
    r1 = (X00 - (q6 * P)) % (1 << (2 * s + 1))  # Step 8: r1 ← X00 mod 2^(2s+1) - (q6 * P) mod 2^(2s+1)
    r2 = (r1 - P)  # Step 9: r2 ← (r1 - P) mod P

    # Step 10: Choose {r ∈ {r1, r2} | 0 ≤ r < P}
    return min(r1, r2)  # Directly return the smaller value in the range

# Example usage
A = 3733
B = 2709
P = 2749

result = Improved_Folding_Barrett_Reduction(A, B, P)
print("Result:", result)
print("Expected:", (A * B) % P)
    

# # Test case 1
# X = 1467 * 2489
# P = 7681

# # Measure computation time
# start_time = time.time()
# result = Improved_Folding_Barrett_Reduction(X, P)
# end_time = time.time()

# computation_time_seconds = end_time - start_time
# computation_time_milliseconds = computation_time_seconds * 1e6

# print("Result:", result)
# print("Computation Time:", computation_time_milliseconds, "microsecond")

# # Test case 2
# X = 1467 * 2489
# P = 10681

# # Measure computation time
# start_time = time.time()
# result = Improved_Folding_Barrett_Reduction(X, P)
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
# result = Improved_Folding_Barrett_Reduction(X, P)
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
# result = Improved_Folding_Barrett_Reduction(X, P)
# end_time = time.time()

# computation_time_seconds = end_time - start_time
# computation_time_milliseconds = computation_time_seconds * 1e6

# print("Result:", result)
# print("Computation Time:", computation_time_milliseconds, "microsecond")