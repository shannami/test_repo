def gcd(a, b):
    while b != 0:
        a, b = d, a % b
    return a
