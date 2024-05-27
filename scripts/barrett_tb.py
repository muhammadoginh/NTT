from General_Barrett_Reduction import *

# Test case 5   # bit length 64
X = 2703006969 * 3572965319
P = 7681

# Measure computation time
start_time = time.time()
result = General_Barrett_Reduction(X, P)
end_time = time.time()

computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6

print("Result:", result)
print("Computation Time:", computation_time_milliseconds, "microsecond")