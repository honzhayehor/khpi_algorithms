import pytest

from euler.tasks.exercise_15 import lattice_paths_dp, lattice_paths_formula

BOTH = [lattice_paths_formula, lattice_paths_dp]


@pytest.mark.parametrize("fn", BOTH)
def test_example_2x2(fn):
    assert fn(2, 2) == 6


@pytest.mark.parametrize("fn", BOTH)
def test_1x1(fn):
    assert fn(1, 1) == 2


@pytest.mark.parametrize("fn", BOTH)
def test_zero_grid(fn):
    assert fn(0, 0) == 1


@pytest.mark.parametrize("fn", BOTH)
def test_single_row_has_one_path_per_shape(fn):
    assert fn(0, 5) == 1
    assert fn(5, 0) == 1


@pytest.mark.parametrize("fn", BOTH)
def test_3x3(fn):
    assert fn(3, 3) == 20


@pytest.mark.parametrize("fn", BOTH)
def test_rectangular_grid(fn):
    assert fn(2, 3) == 10
    assert fn(3, 2) == 10


def test_formula_matches_dp():
    for r in range(0, 12):
        for c in range(0, 12):
            assert lattice_paths_formula(r, c) == lattice_paths_dp(r, c)


@pytest.mark.parametrize("fn", BOTH)
def test_negative_input_raises(fn):
    with pytest.raises(ValueError):
        fn(-1, 2)


@pytest.mark.parametrize("fn", BOTH)
def test_full_answer(fn):
    assert fn(20, 20) == 137846528820