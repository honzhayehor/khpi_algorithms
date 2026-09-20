# Creating Euclidian algorithm (What is the smallest common divider for a and b)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# That is a mirror for gcd (what is the smallest common number that divides evenly by a and b)
def lcm(a, b):
    return a * b // gcd(a, b)

# Returns number that is the smallest one that divides evenly by all numbers between 'starting' and 'to'
def smallest_common(starting: int, to: int):
    result = 1
    for n in range(starting, to + 1 ):
        result = lcm(result, n)
    return result