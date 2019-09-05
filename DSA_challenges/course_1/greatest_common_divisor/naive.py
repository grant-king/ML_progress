"""
input: integer, other integer

output: greatest common divisor of both inputs

approach: increment a divisor variable and test if it can divide both a and b, return highest divisor value
"""

def naive_gcd(a, b):
    greatest_divisor = 1
    for value in range(1, a + b):
        if a % value == 0 and b % value == 0:
            greatest_divisor = value
    return greatest_divisor

