def is_palindrome(n: int) -> bool:
    s = str(n)
    return s == s[::-1]


def largest_palindrome_product(digits: int = 3) -> int:
    if digits < 1:
        raise ValueError("digits must be >= 1")

    low = 10 ** (digits - 1)
    high = 10 ** digits - 1
    best = 0

    for a in range(high, low - 1, -1):
        if a * a <= best:
            break
        for b in range(a, low - 1, -1):
            product = a * b
            if product <= best:
                break
            if is_palindrome(product):
                best = product
                break
    return best
