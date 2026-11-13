def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")

    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def sum_of_digits(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    return sum(int(ch) for ch in str(n))


def factorial_digit_sum(n: int) -> int:
    return sum_of_digits(factorial(n))
