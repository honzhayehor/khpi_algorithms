def special_triplet_product(total: int) -> int | None:
    for a in range(1, total // 3 + 1):
        numerator = total * (total - 2 * a)
        denominator = 2 * (total - a)
        if numerator % denominator == 0:
            b = numerator // denominator
            c = total - a - b
            if a < b < c:
                return a * b * c
    return None
