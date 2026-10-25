def sum_of_n_squares(number_of_elements: int):
    sum_of_elements = 0
    for i in range(1, number_of_elements + 1):
        i_squared = (i ** 2)
        sum_of_elements += i_squared

    return sum_of_elements

def square_of_sum(number_of_elemnts: int):
    sum_of_els = sum([i for i in range(1, number_of_elemnts + 1)])
    return sum_of_els ** 2


def sum_square_difference(number_of_elements: int):
    sqr_of_sum = square_of_sum(number_of_elements)
    sum_of_squares = sum_of_n_squares(number_of_elements)

    return sqr_of_sum - sum_of_squares
