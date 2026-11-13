def series_sum(limit):
    if limit < 1:
        raise ValueError("limit must be >= 1")
    return sum(n ** n for n in range(1, limit + 1))


def last_digits_of_series(limit, digits=10):
    if limit < 1:
        raise ValueError("limit must be >= 1")
    if digits < 1:
        raise ValueError("digits must be >= 1")

    modulus = 10 ** digits
    return sum(pow(n, n, modulus) for n in range(1, limit + 1)) % modulus


def last_digits_text(limit, digits=10):
    return str(last_digits_of_series(limit, digits)).zfill(digits)
