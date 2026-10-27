from math import prod

def largest_product(digits: str, window: int) -> int:
    best = 0
    for i in range(len(digits) - window + 1):
        chunk = digits[i : i + window]
        best = max(best, prod(int(d) for d in chunk))
    return best
