import pytest

from euler.tasks.exercise_9 import special_triplet_product


def test_sum_12_gives_3_4_5_triplet():
    assert special_triplet_product(12) == 3 * 4 * 5


def test_sum_24_gives_6_8_10_triplet():
    assert special_triplet_product(24) == 6 * 8 * 10


def test_sum_30_gives_5_12_13_triplet():
    assert special_triplet_product(30) == 5 * 12 * 13


def test_sum_40_gives_8_15_17_triplet():
    assert special_triplet_product(40) == 8 * 15 * 17


def test_sum_56_gives_7_24_25_triplet():
    assert special_triplet_product(56) == 7 * 24 * 25


def test_sum_with_no_triplet_returns_none():
    assert special_triplet_product(10) is None


@pytest.mark.parametrize("total", [1, 2, 3, 5, 7, 9, 11, 13, 101, 999])
def test_odd_sums_have_no_triplet(total):
    # a + b + c of any Pythagorean triplet is always even
    assert special_triplet_product(total) is None


@pytest.mark.parametrize("total", [0, 1, 2, 3, 4])
def test_very_small_sums_return_none(total):
    assert special_triplet_product(total) is None


def test_sum_1000_has_a_triplet_with_positive_product():
    result = special_triplet_product(1000)
    assert isinstance(result, int)
    assert result > 0


def test_matches_brute_force_for_all_sums_up_to_300():
    def brute_force_products(total):
        products = set()
        for a in range(1, total):
            for b in range(a + 1, total):
                c = total - a - b
                if c > b and a * a + b * b == c * c:
                    products.add(a * b * c)
        return products

    for total in range(1, 301):
        expected = brute_force_products(total)
        result = special_triplet_product(total)
        if expected:
            assert result in expected, f"wrong result for sum {total}"
        else:
            assert result is None, f"expected None for sum {total}"