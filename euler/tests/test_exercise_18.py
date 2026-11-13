import copy
import random
import pytest

from euler.tasks.exercise_18 import max_path_sum, parse_triangle

TRIANGLE_TEXT = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

def brute_force(triangle, row=0, col=0):
    value = triangle[row][col]
    if row == len(triangle) - 1:
        return value
    return value + max(brute_force(triangle, row + 1, col),
                       brute_force(triangle, row + 1, col + 1))


def test_example_from_problem():
    triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    assert max_path_sum(triangle) == 23


def test_single_row():
    assert max_path_sum([[42]]) == 42


def test_two_rows():
    assert max_path_sum([[1], [5, 2]]) == 6


def test_greedy_choice_would_fail():
    triangle = [[1], [2, 3], [10, 1, 1]]
    assert max_path_sum(triangle) == 13


def test_parse_triangle_values_and_shape():
    assert parse_triangle("03\n07 04\n02 04 06") == [[3], [7, 4], [2, 4, 6]]


def test_parse_triangle_rejects_wrong_row_length():
    with pytest.raises(ValueError):
        parse_triangle("1\n2 3 4")


def test_empty_triangle_raises():
    with pytest.raises(ValueError):
        max_path_sum([])


def test_input_is_not_modified():
    triangle = parse_triangle(TRIANGLE_TEXT)
    before = copy.deepcopy(triangle)
    max_path_sum(triangle)
    assert triangle == before


def test_matches_brute_force_on_random_triangles():
    rng = random.Random(0)
    for size in range(1, 11):
        triangle = [[rng.randint(1, 99) for _ in range(i + 1)] for i in range(size)]
        assert max_path_sum(triangle) == brute_force(triangle)


def test_full_answer():
    assert max_path_sum(parse_triangle(TRIANGLE_TEXT)) == 1074