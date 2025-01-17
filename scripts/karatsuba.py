import time

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y  # Base case for small numbers

    # Calculate the number of bits in the maximum input
    n = max(x.bit_length(), y.bit_length())

    # Split the numbers into halves
    half = n // 2
    low1, high1 = x & ((1 << half) - 1), x >> half
    low2, high2 = y & ((1 << half) - 1), y >> half


    # Recursive steps
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    # Combine results using the Karatsuba formula
    return (z2 << (2 * half)) + ((z1 - z2 - z0) << half) + z0

# Example usage
x = 2432654756867985372462134688198654035739486583776581345738651237534898857348566524326547568679853724621346881986540357394865837765813457386512375348988573485665
y = 2980913123453453749865439885734563495743985637646985740387589364588783704563426224326547568679853724621346881986540357394865837765813457386512375348988573485665


start_time = time.time()
x*y
end_time = time.time()
# print(z)
computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6
print("* Computation Time:", computation_time_milliseconds, "microsecond")

start_time = time.time()
karatsuba(x, y)
end_time = time.time()
# print("Result:", result)
computation_time_seconds = end_time - start_time
computation_time_milliseconds = computation_time_seconds * 1e6
print("Karatsuba Computation Time:", computation_time_milliseconds, "microsecond")