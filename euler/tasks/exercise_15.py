from math import comb

def lattice_paths_formula(rows, cols):
    if rows < 0 or cols < 0:
        raise ValueError("rows and cols must be >= 0")
    return comb(rows + cols, rows)


def lattice_paths_dp(rows, cols):
    if rows < 0 or cols < 0:
        raise ValueError("rows and cols must be >= 0")

    ways = [[1] * (cols + 1) for _ in range(rows + 1)]
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            ways[r][c] = ways[r - 1][c] + ways[r][c - 1]
    return ways[rows][cols]
