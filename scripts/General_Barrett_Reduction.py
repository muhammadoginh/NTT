# Resource: https://dx.doi.org/10.1007/3-540-47721-7_24

import math
import time

def General_Barrett_Reduction(X, P):

    # pre-computation
    k = math.ceil(math.log2(P))
    mu = 2**(2*k) // P
    # print(mu)

    # Barrett Reduction
    q1 = X >> k
    print(len(bin(q1)[2:]))
    q2 = q1 * mu
    print(len(bin(q2)[2:]))
    q3 = q2 >> k
    print(len(bin(q3)[2:]))
    r = X - q3*P
    print(len(bin(r)[2:]))
    if r > P:
        r = r - P

    # Barrett Reduction
    # q1 = X * mu
    # print(len(bin(q1)[2:]))
    # q2 = q1 >> (2*k)
    # print(len(bin(q2)[2:]))
    # q3 = q2 * P
    # print(len(bin(q3)[2:]))
    # r = X - q3
    # print(len(bin(r)[2:]))
    # if r > P:
    #     r = r - P

    return(r)

# Test case 1
X = 2270756014 * 2165683850
P = 4294475777

# q_list = vector((576460752340123649, 9007199282003969, 9007199284101121, 9007199318704129, 9007199338627073, 9007199343869953, 9007199350161409));
# p = 9007199379521537;

# Measure computation time
start_time = time.time()
result = General_Barrett_Reduction(X, P)
end_time = time.time()

computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6

print("Expect:", X % P)
print("Result:", result)
print("Computation Time:", computation_time_milliseconds, "microsecond")

# # Test case 2
# X = 1467 * 2489
# # P = 10681

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
# # P = 17681

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
# # P = 56811

# # Measure computation time
# start_time = time.time()
# result = General_Barrett_Reduction(X, P)
# end_time = time.time()

# computation_time_seconds = end_time - start_time
# computation_time_milliseconds = computation_time_seconds * 1e6

# print("Result:", result)
# print("Computation Time:", computation_time_milliseconds, "microsecond")


## input variaton
# # Test case 1
# X = 14820787 * 13250787 # bit length 48
# P = 576460752340123649

# # Measure computation time
# start_time = time.time()
# result = General_Barrett_Reduction(X, P)
# end_time = time.time()

# computation_time_seconds = end_time - start_time
# computation_time_milliseconds = computation_time_seconds * 1e6

# print("Result:", result)
# print("Computation Time:", computation_time_milliseconds, "microsecond")

# # Test case 2
# X = 53299611 * 43577620 # bit length 52
# # P = 7681

# # Measure computation time
# start_time = time.time()
# result = General_Barrett_Reduction(X, P)
# end_time = time.time()

# computation_time_seconds = end_time - start_time
# computation_time_milliseconds = computation_time_seconds * 1e6

# print("Result:", result)
# print("Computation Time:", computation_time_milliseconds, "microsecond")

# # Test case 3   # bit length 56
# X = 183698636 * 199698586
# # P = 7681

# # Measure computation time
# start_time = time.time()
# result = General_Barrett_Reduction(X, P)
# end_time = time.time()

# computation_time_seconds = end_time - start_time
# computation_time_milliseconds = computation_time_seconds * 1e6

# print("Result:", result)
# print("Computation Time:", computation_time_milliseconds, "microsecond")

# # Test case 4   # bit length 60
# X = 790536324 * 774867031
# # P = 7681

# # Measure computation time
# start_time = time.time()
# result = General_Barrett_Reduction(X, P)
# end_time = time.time()

# computation_time_seconds = end_time - start_time
# computation_time_milliseconds = computation_time_seconds * 1e6

# print("Result:", result)
# print("Computation Time:", computation_time_milliseconds, "microsecond")


