"""
Project Euler 16 - Power Digit Sum
Find the sum of the digits of 2**1000.

Two approaches:
  1. brute_force()  - let Python compute 2**n, turn it into text, add the digits
  2. smart()        - never use a big integer; store the number as a list of
                      digits and double it n times by hand (like on paper)
"""

EXPONENT = 1000


# ---------------------------------------------------------------------------
# Route 1: Brute force
# ---------------------------------------------------------------------------
def brute_force(exponent: int) -> int:
    """Compute 2**exponent directly, then add up its digits.

    Python ints have arbitrary precision, so 2**1000 (302 digits) is exact.
    str() turns the number into text, and each character is one digit.
    """
    number = 2 ** exponent
    return sum(int(ch) for ch in str(number))


# ---------------------------------------------------------------------------
# Route 2: Smart approach (manual big-number arithmetic)
# ---------------------------------------------------------------------------
def double_digits(digits: list) -> list:
    """Multiply a number by 2, where the number is a list of digits.

    The digits are stored in REVERSE order (least significant first), so
    [8, 6, 7, 2, 3] means 32768. This makes carrying easy: we move left to
    right through the list, exactly like doing the multiplication on paper
    from the right-hand side.

    Example: 32768 * 2
        8*2 = 16 -> write 6, carry 1
        6*2 +1 = 13 -> write 3, carry 1
        7*2 +1 = 15 -> write 5, carry 1
        2*2 +1 = 5  -> write 5, carry 0
        3*2    = 6  -> write 6, carry 0
        result: [6, 3, 5, 5, 6] = 65536
    """
    result = []
    carry = 0
    for d in digits:
        value = d * 2 + carry
        result.append(value % 10)
        carry = value // 10
    if carry:
        result.append(carry)
    return result


def smart(exponent: int) -> int:
    """Compute the digit sum of 2**exponent without big integers or strings.

    Start with the number 1 and double it `exponent` times. Each doubling only
    touches single digits (0-9), so no number ever gets bigger than 19.
    """
    digits = [1]
    for _ in range(exponent):
        digits = double_digits(digits)
    return sum(digits)
