from naive import naive_gcd
from fast import euclid_gcd

def test_naive_gcd():
    assert naive_gcd(15, 66) == 3

def test_naive_gcd_long_input():
    assert naive_gcd(10000000, 1000000) == 1000000

def test_naive_gcd_long_agian():
    assert naive_gcd(3918848, 1653264) == 61232

def test_euclid_gcd():
    assert euclid_gcd(15, 66) == 3

def test_euclid_gcd_long():
    assert euclid_gcd(1000000000, 1000000) == 1000000

def test_euclid_gcd_long_agian():
    assert euclid_gcd(3918848, 1653264) == 61232

