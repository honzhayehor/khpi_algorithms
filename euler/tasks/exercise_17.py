NUMBER_LENGTHS = {
    0: 0,    # nothing is said for a zero part, e.g. the "zero" in 305
    1: 3,    # one
    2: 3,    # two
    3: 5,    # three
    4: 4,    # four
    5: 4,    # five
    6: 3,    # six
    7: 5,    # seven
    8: 5,    # eight
    9: 4,    # nine
    10: 3,   # ten
    11: 6,   # eleven
    12: 6,   # twelve
    13: 8,   # thirteen
    14: 8,   # fourteen
    15: 7,   # fifteen
    16: 7,   # sixteen
    17: 9,   # seventeen
    18: 8,   # eighteen
    19: 8,   # nineteen
    20: 6,   # twenty
    30: 6,   # thirty
    40: 5,   # forty
    50: 5,   # fifty
    60: 5,   # sixty
    70: 7,   # seventy
    80: 6,   # eighty
    90: 6,   # ninety
}
HUNDRED = 7
THOUSAND = 8
AND = 3

def letters_below_100(number):
    if number < 20:
        return NUMBER_LENGTHS[number]
    tens, ones = divmod(number, 10)
    return NUMBER_LENGTHS[tens * 10] + NUMBER_LENGTHS[ones]

def number_to_letter_count(number):
    if not 1 <= number <= 1000:
        raise ValueError("number must be between 1 and 1000")
    if number == 1000:
        return NUMBER_LENGTHS[1] + THOUSAND

    hundreds, rest = divmod(number, 100)
    total = letters_below_100(rest)
    if hundreds:
        total += NUMBER_LENGTHS[hundreds] + HUNDRED
        if rest:
            total += AND
    return total

def number_letter_counts(up_to):
    return sum(number_to_letter_count(n) for n in range(1, up_to + 1))

