import pytest

from euler.tasks.exercise_1 import (
    sum_of_elements,
    get_all_divisible,
    get_sum_of_divisible,
)

def test_sum_of_elements_basic():
    assert sum_of_elements([1, 2, 3]) == 6


def test_sum_of_elements_empty():
    assert sum_of_elements([]) == 0


# ---------- get_all_divisible: single int divisor ----------

def test_single_divisor_basic():
    assert get_all_divisible(3, 1, 10) == [3, 6, 9]


def test_single_divisor_none_found():
    assert get_all_divisible(11, 1, 10) == []


def test_single_divisor_exclusive_upper_bound():
    # ending_number itself must NOT be included even if divisible
    result = get_all_divisible(5, 1, 10)
    assert 10 not in result
    assert result == [5]


def test_single_divisor_start_equal_end_raises():
    with pytest.raises(ValueError):
        get_all_divisible(3, 5, 5)


def test_single_divisor_start_greater_than_end_raises():
    with pytest.raises(ValueError):
        get_all_divisible(3, 10, 5)


# ---------- get_all_divisible: list of divisors ----------

def test_list_divisor_union_no_double_counting():
    # 15 is divisible by both 3 and 5, must appear only once
    result = get_all_divisible([3, 5], 1, 20)
    assert result == [3, 5, 6, 9, 10, 12, 15, 18]
    assert result.count(15) == 1


def test_list_divisor_matches_single_divisor_case():
    # a one-element list should behave like the plain-int path
    assert get_all_divisible([3], 1, 10) == get_all_divisible(3, 1, 10)


def test_list_divisor_empty_list_returns_empty():
    assert get_all_divisible([], 1, 10) == []


def test_list_divisor_result_is_plain_ints_not_numpy_types():
    result = get_all_divisible([3, 5], 1, 20)
    assert all(isinstance(x, int) for x in result)


# ---------- get_all_divisible: invalid divisor type ----------

def test_invalid_divisor_type_raises_value_error():
    with pytest.raises(ValueError):
        get_all_divisible("3", 1, 10)  # string is neither int nor list


def test_invalid_divisor_type_dict_raises_value_error():
    with pytest.raises(ValueError):
        get_all_divisible({3: 5}, 1, 10)


# ---------- get_sum_of_divisible (end to end) ----------

def test_sum_of_divisible_single_divisor():
    assert get_sum_of_divisible(1, 10, 3) == 18  # 3 + 6 + 9


def test_sum_of_divisible_project_euler_1():
    # classic check: sum of multiples of 3 or 5 below 1000 == 233168
    assert get_sum_of_divisible(0, 1000, [3, 5]) == 233168


def test_sum_of_divisible_matches_brute_force():
    divisors = [3, 5, 7]
    expected = sum(i for i in range(0, 500) if any(i % d == 0 for d in divisors))
    assert get_sum_of_divisible(0, 500, divisors) == expected


def test_sum_of_divisible_empty_range_raises():
    with pytest.raises(ValueError):
        get_sum_of_divisible(5, 5, [3, 5])