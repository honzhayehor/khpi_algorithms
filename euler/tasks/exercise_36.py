def is_palindrome(text):
    return text == text[::-1]


def is_double_base_palindrome(n):
    return is_palindrome(str(n)) and is_palindrome(bin(n)[2:])


def double_base_numbers_brute(limit):
    if limit < 1:
        raise ValueError("limit must be >= 1")
    return [n for n in range(1, limit, 2) if is_double_base_palindrome(n)]


def decimal_palindromes_below(limit):
    if limit < 1:
        raise ValueError("limit must be >= 1")

    digits = len(str(limit - 1))
    palindromes = []
    for half in range(1, 10 ** ((digits + 1) // 2)):
        text = str(half)
        for candidate in (text + text[-2::-1], text + text[::-1]):
            if int(candidate) < limit:
                palindromes.append(int(candidate))
    return sorted(set(palindromes))


def double_base_numbers_smart(limit):
    return [n for n in decimal_palindromes_below(limit) if is_palindrome(bin(n)[2:])]


def sum_of_double_base_palindromes(limit=1_000_000):
    return sum(double_base_numbers_smart(limit))
