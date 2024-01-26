def ntt(a, w, q):
    n = len(a)
    if n == 1:
        return a

    a0 = a[::2]
    a1 = a[1::2]

    w_power = 1
    w_squared = pow(w, 2, q)

    y = ntt(a0, w_squared, q)
    z = ntt(a1, w_squared, q)

    result = [0] * n

    for i in range(n // 2):
        t = (w_power * z[i]) % q
        result[i] = (y[i] + t) % q
        result[i + n // 2] = (y[i] - t) % q

        w_power = (w_power * w) % q

    return result

# Example usage
a = [1, 2, 3, 4]
q = 7681
w = 3383  # primitive root of unity, choose an appropriate value based on the modulus

result_ntt = ntt(a, w, q)
print(result_ntt)


def intt(a, w, q):
    w_inv = pow(w, -1, q)
    return [x % q for x in ntt(a, w_inv, q)]

# Example usage
a = [1, 2, 3, 4]
q = 7681
w = 3  # primitive root of unity, choose an appropriate value based on the modulus

# NTT
result_ntt = ntt(a, w, q)
print("NTT:", result_ntt)

# INTT
result_intt = intt(result_ntt, w, q)
print("INTT:", result_intt)


def neg_wrapped_convolution_ntt(a, psi, q):
    n = len(a)
    if n == 1:
        return a

    a0 = a[:n//2]
    a1 = a[n//2:]

    psi_squared = [(x * x) % q for x in psi]

    y = neg_wrapped_convolution_ntt(a0, psi_squared, q)
    z = neg_wrapped_convolution_ntt(a1, psi_squared, q)

    result = [0] * n
    psi_power = 1

    for i in range(n // 2):
        t = (psi_power * z[i]) % q
        result[i] = (y[i] + t) % q  # Adjusted sign for negative wrapped convolution
        result[i + n // 2] = (y[i] - t) % q  # Adjusted sign for negative wrapped convolution

        psi_power = (psi_power * psi[i]) % q

    return result

# Example usage
a = [1, 2, 3, 4]
psi = [1, 1925, 3383, 6468]
q = 7681

result_neg_wrapped_conv_ntt = neg_wrapped_convolution_ntt(a, psi, q)
print("Negative Wrapped Convolution NTT:", result_neg_wrapped_conv_ntt)
