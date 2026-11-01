from math import prod


def parse_grid(text: str):
    rows = [list(map(int, line.split())) for line in text.strip().splitlines() if line.strip()]
    if rows and any(len(r) != len(rows[0]) for r in rows):
        raise ValueError("All rows must have the same length")
    return rows

def largest_product(grid, length=4):

    DIRECTIONS = {
        "right": (0, 1),
        "down": (1, 0),
        "diag_down_right": (1, 1),
        "diag_down_left": (1, -1),
    }

    if length < 1:
        raise ValueError("length must be >= 1")
    if not grid or not grid[0]:
        raise ValueError("grid must not be empty")

    n_rows, n_cols = len(grid), len(grid[0])
    best = None

    for r in range(n_rows):
        for c in range(n_cols):
            for name, (dr, dc) in DIRECTIONS.items():
                end_r, end_c = r + (length - 1) * dr, c + (length - 1) * dc
                if not (0 <= end_r < n_rows and 0 <= end_c < n_cols):
                    continue
                cells = tuple(grid[r + i * dr][c + i * dc] for i in range(length))
                p = prod(cells)
                if best is None or p > best[0]:
                    best = (p, cells, (r, c), name)

    if best is None:
        raise ValueError("grid is too small for the requested length")
    return best
