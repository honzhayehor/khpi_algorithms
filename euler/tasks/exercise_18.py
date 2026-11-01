def parse_triangle(text):
    rows = [list(map(int, line.split())) for line in text.strip().splitlines() if line.strip()]
    for i, row in enumerate(rows):
        if len(row) != i + 1:
            raise ValueError(f"Row {i} must have {i + 1} numbers, got {len(row)}")
    return rows


def max_path_sum(triangle):
    if not triangle:
        raise ValueError("triangle must not be empty")

    best = list(triangle[-1])
    for row in reversed(triangle[:-1]):
        best = [value + max(best[i], best[i + 1]) for i, value in enumerate(row)]
    return best[0]

