import pytest

from euler.tasks.exerciese_12 import count_divisors, first_triangle_over, triangle_number


def test_first_ten_triangle_numbers():
    assert [triangle_number(n) for n in range(1, 11)] == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]


def test_triangle_number_invalid():
    with pytest.raises(ValueError):
        triangle_number(0)


def test_count_divisors_of_one():
    assert count_divisors(1) == 1


def test_count_divisors_of_prime():
    assert count_divisors(13) == 2


def test_count_divisors_of_28():
    # 1, 2, 4, 7, 14, 28
    assert count_divisors(28) == 6


def test_count_divisors_perfect_square():
    # 1, 2, 3, 4, 6, 9, 12, 18, 36
    assert count_divisors(36) == 9


def test_count_divisors_matches_brute_force():
    for n in range(1, 200):
        expected = sum(1 for d in range(1, n + 1) if n % d == 0)
        assert count_divisors(n) == expected


def test_count_divisors_invalid():
    with pytest.raises(ValueError):
        count_divisors(0)


def test_example_from_problem():
    assert first_triangle_over(5) == 28


def test_full_answer():
    assert first_triangle_over(500) == 76576500