# (row change, column change): right, down, left, up
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def spiral_positions(size):
    if size < 1 or size % 2 == 0:
        raise ValueError("size must be an odd number >= 1")

    total = size * size
    row = col = size // 2
    yield row, col
    visited = 1

    run_length = 1
    direction = 0
    while visited < total:
        for _ in range(2):
            d_row, d_col = DIRECTIONS[direction % 4]
            for _ in range(run_length):
                if visited == total:
                    return
                row += d_row
                col += d_col
                yield row, col
                visited += 1
            direction += 1
        run_length += 1

def build_spiral(size):
    grid = [[0] * size for _ in range(size)]
    for number, (row, col) in enumerate(spiral_positions(size), start=1):
        grid[row][col] = number
    return grid


def sum_of_diagonals(grid):
    size = len(grid)
    if size == 0 or any(len(row) != size for row in grid):
        raise ValueError("grid must be square and not empty")

    total = 0
    for i in range(size):
        total += grid[i][i]
        total += grid[i][size - 1 - i]

    if size % 2 == 1:
        center = size // 2
        total -= grid[center][center]
    return total


def spiral_diagonal_sum(size):
    return sum_of_diagonals(build_spiral(size))
