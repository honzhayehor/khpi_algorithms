def sum_of_primes_below(limit: int) -> int:
    if limit <= 2:
        return 0
    sieve = bytearray([1]) * limit
    sieve[:2] = b"\x00\x00"
    for i in range(2, int((limit - 1) ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(range(i * i, limit, i)))
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)
