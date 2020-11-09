"""
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""


def get_perfect_number(n):
    if n <= 0:
        return
    return n * 10 + 10 - n


assert get_perfect_number(1) == 19
assert get_perfect_number(2) == 28
assert get_perfect_number(3) == 37
