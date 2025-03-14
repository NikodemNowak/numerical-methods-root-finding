def horner(x, coeffs, n):
    result = coeffs[0]
    for i in range(1, n):
        result = result * x + coeffs[i]
    return result