from euler.tasks.exercise_6 import sum_of_n_squares, square_of_sum, sum_square_difference

def test_sum_square_difference_for_base_case():
    assert sum_square_difference(10) == 2640

def test_square_of_sum_for_base_case():
    assert square_of_sum(10) == 3025

def test_sum_of_squares_for_base():
    assert sum_of_n_squares(10) == 385

def test_sum_square_difference_for_100():
    assert sum_square_difference(100) == 25164150

