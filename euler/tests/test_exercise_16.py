import pytest
from euler.tasks.exercise_16 import brute_force, double_digits, smart

def test_example_from_problem_statement():
    """2**15 = 32768 and 3+2+7+6+8 = 26."""
    assert brute_force(15) == 26
    assert smart(15) == 26


def test_final_answer():
    """The answer for the real problem (2**1000)."""
    assert brute_force(1000) == 1366
    assert smart(1000) == 1366

@pytest.mark.parametrize(
    "exponent, expected",
    [
        (0, 1),    # 1
        (1, 2),    # 2
        (3, 8),    # 8
        (4, 7),    # 16 -> 1+6
        (10, 7),   # 1024 -> 1+0+2+4
        (15, 26),  # 32768
    ],
)
def test_known_values(exponent, expected):
    assert brute_force(exponent) == expected
    assert smart(exponent) == expected


# ---------------------------------------------------------------------------
# double_digits (digits are stored in reverse: [8, 6, 7, 2, 3] = 32768)
# ---------------------------------------------------------------------------
def test_double_no_carry():
    assert double_digits([1]) == [2]          # 1 -> 2


def test_double_single_carry():
    assert double_digits([6, 1]) == [2, 3]    # 16 -> 32


def test_double_grows_by_one_digit():
    assert double_digits([5]) == [0, 1]       # 5 -> 10
    assert double_digits([9, 9]) == [8, 9, 1] # 99 -> 198


def test_double_example_from_docstring():
    assert double_digits([8, 6, 7, 2, 3]) == [6, 3, 5, 5, 6]  # 32768 -> 65536


def test_double_does_not_modify_input():
    original = [8, 6, 7, 2, 3]
    double_digits(original)
    assert original == [8, 6, 7, 2, 3]


@pytest.mark.parametrize("n", [0, 1, 7, 50, 123, 999, 123456789])
def test_double_matches_integer_doubling(n):
    """Doubling the digit list must give the same number as n * 2."""
    digits = [int(ch) for ch in reversed(str(n))]
    doubled = double_digits(digits)
    as_number = int("".join(str(d) for d in reversed(doubled)))
    assert as_number == n * 2


# ---------------------------------------------------------------------------
# Size of the result
# ---------------------------------------------------------------------------
def test_2_to_the_1000_has_302_digits():
    """The number of digits of 2**1000 is 302; the manual version must agree."""
    digits = [1]
    for _ in range(1000):
        digits = double_digits(digits)
    assert len(digits) == 302
    assert len(str(2 ** 1000)) == 302