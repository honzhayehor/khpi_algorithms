from itertools import combinations_with_replacement


def digit_power_sum(n, power):
    return sum(int(ch) ** power for ch in str(n))


def max_digits(power):
    if power < 1:
        raise ValueError("power must be >= 1")

    n = 1
    while 10 ** n <= (n + 1) * 9 ** power:
        n += 1
    return n


def search_limit(power):
    return max_digits(power) * 9 ** power


def numbers_brute(power):
    return [n for n in range(10, search_limit(power) + 1) if n == digit_power_sum(n, power)]


def numbers_multisets(power):
    found = set()
    for length in range(2, max_digits(power) + 1):
        for digits in combinations_with_replacement(range(10), length):
            total = sum(d ** power for d in digits)
            if tuple(sorted(int(ch) for ch in str(total))) == digits:
                found.add(total)
    return sorted(found)


def sum_of_digit_power_numbers(power=5):
    return sum(numbers_multisets(power))
