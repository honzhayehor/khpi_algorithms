import pytest

from euler.tasks.exercise_28 import spiral_diagonal_sum, sum_of_diagonals,build_spiral

def test_example_5x5_spiral_from_problem():
    assert sum_of_diagonals(build_spiral(5)) == 101


def test_single_cell():
    assert sum_of_diagonals([[7]]) == 7


def test_center_is_counted_once_for_odd_sizes():
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    assert sum_of_diagonals(grid) == 25


def test_even_grid_has_no_shared_center():
    grid = [[1, 2],
            [3, 4]]
    assert sum_of_diagonals(grid) == 10


def test_only_diagonal_cells_matter():
    grid = [[1, 0, 3],
            [0, 5, 0],
            [7, 0, 9]]
    changed = [[1, 99, 3],
               [-4, 5, 8],
               [7, 55, 9]]
    assert sum_of_diagonals(grid) == sum_of_diagonals(changed) == 25


@pytest.mark.parametrize("size, expected", [(3, 25), (7, 261), (9, 537)])
def test_small_spirals(size, expected):
    assert spiral_diagonal_sum(size) == expected


def test_matches_corner_formula():
    for size in range(1, 52, 2):
        rings = (size - 1) // 2
        expected = 1 + sum(4 * (2 * k + 1) ** 2 - 12 * k for k in range(1, rings + 1))
        assert spiral_diagonal_sum(size) == expected


def test_non_square_grid_raises():
    with pytest.raises(ValueError):
        sum_of_diagonals([[1, 2, 3], [4, 5, 6]])


def test_empty_grid_raises():
    with pytest.raises(ValueError):
        sum_of_diagonals([])


def test_full_answer():
    assert spiral_diagonal_sum(1001) == 669171001