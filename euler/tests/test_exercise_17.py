import pytest

from euler.tasks.exercise_17 import letters_below_100, number_letter_counts, number_to_letter_count


def test_example_one_to_five():
    assert number_letter_counts(5) == 19


def test_examples_from_problem_note():
    assert number_to_letter_count(342) == 23
    assert number_to_letter_count(115) == 20


@pytest.mark.parametrize("number, word", [
    (11, "eleven"), (12, "twelve"), (13, "thirteen"), (14, "fourteen"),
    (15, "fifteen"), (16, "sixteen"), (17, "seventeen"), (18, "eighteen"),
    (19, "nineteen"),
])
def test_teens_are_looked_up_as_one_word(number, word):
    assert number_to_letter_count(number) == len(word)


@pytest.mark.parametrize("number, word", [
    (21, "twentyone"), (42, "fortytwo"), (77, "seventyseven"), (99, "ninetynine"),
])
def test_tens_plus_ones(number, word):
    assert number_to_letter_count(number) == len(word)


@pytest.mark.parametrize("number, word", [
    (20, "twenty"), (40, "forty"), (70, "seventy"), (90, "ninety"),
])
def test_round_tens_have_no_ones_part(number, word):
    assert letters_below_100(number) == len(word)


@pytest.mark.parametrize("number, word", [
    (100, "onehundred"), (300, "threehundred"), (900, "ninehundred"),
])
def test_round_hundreds_have_no_and(number, word):
    assert number_to_letter_count(number) == len(word)


@pytest.mark.parametrize("number, word", [
    (101, "onehundredandone"), (110, "onehundredandten"), (999, "ninehundredandninetynine"),
])
def test_hundreds_with_remainder_have_and(number, word):
    assert number_to_letter_count(number) == len(word)


def test_one_thousand():
    assert number_to_letter_count(1000) == len("onethousand")


def test_out_of_range_raises():
    with pytest.raises(ValueError):
        number_to_letter_count(0)
    with pytest.raises(ValueError):
        number_to_letter_count(1001)


def test_full_answer():
    assert number_letter_counts(1000) == 21124