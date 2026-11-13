"""
Project Euler 29 - Distinct Powers
Count distinct values of a**b for 2 <= a <= LIMIT and 2 <= b <= LIMIT.

Two approaches:
  1. brute_force()  - compute every a**b and let a set remove duplicates
  2. smart()        - never compute a**b; count distinct (root, exponent) pairs
"""

LIMIT = 100


# ---------------------------------------------------------------------------
# Route 1: Brute force
# ---------------------------------------------------------------------------
def brute_force(limit: int) -> int:
    """Compute every a**b exactly and count the unique results.

    Python ints have arbitrary precision, so even 100**100 is exact.
    A set stores each value once, so duplicates (e.g. 2**4 and 4**2)
    collapse automatically.
    """
    seen = set()
    for a in range(2, limit + 1):
        for b in range(2, limit + 1):
            seen.add(a ** b)
    return len(seen)


# ---------------------------------------------------------------------------
# Route 2: Smart approach
# ---------------------------------------------------------------------------
def find_perfect_powers(limit: int) -> set:
    """Return all numbers in 2..limit that are a perfect power of a smaller number.

    Example for limit=100: {4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100}
    These are NOT "family roots"; they belong to the family of a smaller number.
    """
    perfect_powers = set()
    for r in range(2, limit + 1):
        p = r * r
        while p <= limit:
            perfect_powers.add(p)
            p *= r
    return perfect_powers


def family_size(root: int, limit: int) -> int:
    """Return k = how many powers of `root` fit in 2..limit.

    Example: root=2, limit=100 -> 2, 4, 8, 16, 32, 64 -> k = 6
             root=5, limit=100 -> 5, 25                -> k = 2
             root=11, limit=100 -> 11                  -> k = 1
    """
    k = 1
    p = root
    while p * root <= limit:
        p *= root
        k += 1
    return k


def count_distinct_exponents(k: int, limit: int) -> int:
    """Count distinct exponents i*b for a family of size k.

    A base root**i raised to b equals root**(i*b), so two results in the same
    family are equal exactly when i*b is equal. We only need to count the
    distinct products, which are small numbers (at most k*limit).
    """
    exponents = set()
    for i in range(1, k + 1):
        for b in range(2, limit + 1):
            exponents.add(i * b)
    return len(exponents)


def smart(limit: int) -> int:
    """Count distinct powers without ever computing a huge a**b.

    Steps:
      1. Find which numbers are perfect powers (they join another family).
      2. Every remaining number is a family root; find its family size k.
      3. Count distinct exponents for that k (cached, since it depends only on k).
      4. Different families can never collide, so just add the counts up.
    """
    perfect_powers = find_perfect_powers(limit)
    cache = {}
    total = 0

    for r in range(2, limit + 1):
        if r in perfect_powers:
            continue
        k = family_size(r, limit)
        if k not in cache:
            cache[k] = count_distinct_exponents(k, limit)
        total += cache[k]

    return total