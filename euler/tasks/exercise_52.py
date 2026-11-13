def same_digits(a, b):
    return sorted(str(a)) == sorted(str(b))


def all_multiples_share_digits(x, up_to=6):
    return all(same_digits(x, k * x) for k in range(2, up_to + 1))


def smallest_permuted_multiple(up_to=6):
    if up_to < 1:
        raise ValueError("up_to must be >= 1")

    step = 9 if up_to >= 2 else 1
    length = 1
    while True:
        low = 10 ** (length - 1)
        high = (10 ** length - 1) // up_to
        first = -(-low // step) * step
        for x in range(first, high + 1, step):
            if all_multiples_share_digits(x, up_to):
                return x
        length += 1


def smallest_permuted_multiple_brute(up_to=6):
    x = 1
    while not all_multiples_share_digits(x, up_to):
        x += 1
    return x
