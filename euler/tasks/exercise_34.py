from itertools import combinations_with_replacement
from math import factorial

FACTORIALS = [factorial(d) for d in range(10)]


def digit_factorial_sum(n):
    return sum(FACTORIALS[int(ch)] for ch in str(n))


def max_digits():
    n = 1
    while 10 ** n <= (n + 1) * FACTORIALS[9]:
        n += 1
    return n


def search_limit():
    return max_digits() * FACTORIALS[9]


def curious_numbers_brute(limit):
    return [n for n in range(10, limit + 1) if n == digit_factorial_sum(n)]


def curious_numbers_multisets(length_limit=None):
    if length_limit is None:
        length_limit = max_digits()

    found = []
    for length in range(2, length_limit + 1):
        for digits in combinations_with_replacement(range(10), length):
            total = sum(FACTORIALS[d] for d in digits)
            if tuple(sorted(int(ch) for ch in str(total))) == digits:
                found.append(total)
    return sorted(set(found))


def sum_of_curious_numbers():
    return sum(curious_numbers_multisets())
