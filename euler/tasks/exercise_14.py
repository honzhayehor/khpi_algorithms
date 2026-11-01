def collatz_next(n):
    if n < 1:
        raise ValueError("n must be >= 1")
    return n // 2 if n % 2 == 0 else 3 * n + 1


def collatz_length(n, cache=None):
    if n < 1:
        raise ValueError("n must be >= 1")
    if cache is None:
        cache = {}

    path = []
    while n != 1 and n not in cache:
        path.append(n)
        n = collatz_next(n)

    base = cache.get(n, 1)
    for steps_back, value in enumerate(reversed(path), start=1):
        cache[value] = base + steps_back
    return base + len(path)


def longest_collatz_start(limit):
    if limit < 2:
        raise ValueError("limit must be >= 2")

    cache = {}
    best_start, best_length = 1, 1
    for start in range(2, limit):
        length = collatz_length(start, cache)
        if length > best_length:
            best_start, best_length = start, length
    return best_start, best_length
