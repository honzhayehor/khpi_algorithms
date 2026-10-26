def nth_prime_trial(n: int) -> int:
    primes = [2]
    candidate = 3
    while len(primes) < n:
        if all(candidate % p for p in primes if p * p <= candidate):
            primes.append(candidate)
        candidate += 2
    return primes[-1]
