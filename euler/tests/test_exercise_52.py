import pytest

from euler.tasks.exercise_52 import (
    all_multiples_share_digits,
    same_digits,
    smallest_permuted_multiple,
    smallest_permuted_multiple_brute,
)


def test_example_from_problem():
    assert same_digits(125874, 251748)


def test_same_digits_false_cases():
    assert not same_digits(123, 124)
    assert not same_digits(112, 122)
    assert not same_digits(12, 120)


def test_known_solution_passes_the_check():
    assert all_multiples_share_digits(142857, 6)


def test_125874_works_for_double_only():
    assert all_multiples_share_digits(125874, 2)
    assert not all_multiples_share_digits(125874, 3)


def test_smallest_for_x_and_2x():
    assert smallest_permuted_multiple(2) == 125874


def test_up_to_one_is_trivial():
    assert smallest_permuted_multiple(1) == 1


@pytest.mark.parametrize("up_to", [2, 3, 4, 5, 6])
def test_smart_search_matches_brute_force(up_to):
    assert smallest_permuted_multiple(up_to) == smallest_permuted_multiple_brute(up_to)


def test_result_starts_with_one():
    assert str(smallest_permuted_multiple(6))[0] == "1"


def test_invalid_input_raises():
    with pytest.raises(ValueError):
        smallest_permuted_multiple(0)


def test_full_answer():
    x = smallest_permuted_multiple(6)
    assert x == 142857
    assert [k * x for k in range(1, 7)] == [142857, 285714, 428571, 571428, 714285, 857142]