from itertools import islice

import pytest

from euler.tasks.exercise_25 import fibonacci, find_index_of_element, get_number_length


def test_first_twelve_terms_match_problem():
    assert list(islice(fibonacci(), 12)) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]


def test_generators_are_independent():
    first, second = fibonacci(), fibonacci()
    assert [next(first) for _ in range(5)] == [1, 1, 2, 3, 5]
    assert next(second) == 1


def test_generator_keeps_its_state():
    fib = fibonacci()
    values = [next(fib) for _ in range(6)]
    assert values == [1, 1, 2, 3, 5, 8]


@pytest.mark.parametrize("number, expected", [(0, 1), (5, 1), (144, 3), (10**999, 1000)])
def test_get_number_length(number, expected):
    assert get_number_length(number) == expected


def test_example_from_problem_three_digits():
    assert find_index_of_element(3) == 12

def test_one_digit_returns_first_index():
    assert find_index_of_element(1) == 1


@pytest.mark.parametrize("digits, expected_index", [(2, 7), (4, 17)])
def test_other_digit_counts(digits, expected_index):
    # F7 = 13, F17 = 1597
    assert find_index_of_element(digits) == expected_index


def test_found_term_is_the_first_with_that_many_digits():
    for digits in range(1, 60):
        index = find_index_of_element(digits)
        terms = list(islice(fibonacci(), index))
        assert get_number_length(terms[-1]) == digits
        assert all(get_number_length(t) < digits for t in terms[:-1])


def test_invalid_digit_count_raises():
    with pytest.raises(ValueError):
        find_index_of_element(0)


def test_full_answer():
    assert find_index_of_element(1000) == 4782