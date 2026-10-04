import pytest

from euler.tasks.exercise_29 import (
    brute_force,
    count_distinct_exponents,
    family_size,
    find_perfect_powers,
    smart,
)


# ---------------------------------------------------------------------------
# Whole-solution tests
# ---------------------------------------------------------------------------
def test_example_from_problem_statement():
    """The 5x5 example in the problem has 15 distinct terms."""
    assert brute_force(5) == 15
    assert smart(5) == 15


def test_final_answer():
    """The answer for the real problem (limit 100)."""
    assert brute_force(100) == 9183
    assert smart(100) == 9183


@pytest.mark.parametrize("limit", range(2, 41))
def test_smart_matches_brute_force(limit):
    """The smart approach must agree with brute force for many limits."""
    assert smart(limit) == brute_force(limit)


def test_smallest_limit():
    """Limit 2: only 2**2 = 4, so exactly one value."""
    assert brute_force(2) == 1
    assert smart(2) == 1


# ---------------------------------------------------------------------------
# find_perfect_powers
# ---------------------------------------------------------------------------
def test_perfect_powers_up_to_100():
    expected = {4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100}
    assert find_perfect_powers(100) == expected


def test_perfect_powers_small_limit():
    assert find_perfect_powers(3) == set()
    assert find_perfect_powers(4) == {4}


# ---------------------------------------------------------------------------
# family_size
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "root, expected",
    [
        (2, 6),    # 2, 4, 8, 16, 32, 64
        (3, 4),    # 3, 9, 27, 81
        (5, 2),    # 5, 25
        (6, 2),    # 6, 36
        (7, 2),    # 7, 49
        (10, 2),   # 10, 100
        (11, 1),   # only 11
        (100, 1),  # only itself, since 100*100 > 100
    ],
)
def test_family_size(root, expected):
    assert family_size(root, 100) == expected


# ---------------------------------------------------------------------------
# count_distinct_exponents
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "k, expected",
    [
        (1, 99),   # exponents 2..100
        (2, 149),  # 2..100 plus even numbers 102..200
        (4, 240),
        (6, 328),
    ],
)
def test_count_distinct_exponents(k, expected):
    """These are the per-family counts from the hand calculation."""
    assert count_distinct_exponents(k, 100) == expected


def test_distinct_exponents_small_case():
    """k=2, limit=5: i*b gives {2,3,4,5} and {4,6,8,10} -> {2,3,4,5,6,8,10}."""
    assert count_distinct_exponents(2, 5) == 7


# ---------------------------------------------------------------------------
# Cross-check of the hand calculation breakdown
# ---------------------------------------------------------------------------
def test_hand_calculation_breakdown():
    total = 81 * 99 + 4 * 149 + 240 + 328
    assert total == 9183