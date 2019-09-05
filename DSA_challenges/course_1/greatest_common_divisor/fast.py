"""
input: integer, other integer

output: greatest common divisor of both inputs

approach: increment a divisor variable and test if it can divide both a and b, return highest divisor value
"""

def euclid_gcd(a, b):
    if b == 0:
        return a
    a_prime = a % b
    return euclid_gcd(b, a_prime)
