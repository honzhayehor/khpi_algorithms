def triangle_number(n):
    if n < 1:
        raise ValueError("n must be >= 1")
    return n * (n + 1) // 2

def count_divisors(n):

    if n < 1:
        raise ValueError("n must be >= 1")

    total = 1
    p = 2
    while p * p <= n:
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        total *= exponent + 1
        p += 1
    if n > 1:
        total *= 2
    return total


def first_triangle_over(min_divisors):
    if min_divisors < 0:
        raise ValueError("min_divisors must be >= 0")

    n = 1
    while True:
        t = triangle_number(n)
        if count_divisors(t) > min_divisors:
            return t
        n += 1
