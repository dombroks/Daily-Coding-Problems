"""
This problem was asked by Facebook.

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0
"""


def get_result(x, y, b):
    return x * b + y * abs(b - 1)


assert get_result(5, 2, 0) == 2
assert get_result(10, 11, 1) == 10
