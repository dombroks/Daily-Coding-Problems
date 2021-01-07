"""
Given a real number n, find the square root of n. For example, given n = 9, return 3.
"""
from math import pow


def square_root(n):
    return pow(n, 1 / 2)


assert square_root(9) == 3
assert square_root(49) == 7
