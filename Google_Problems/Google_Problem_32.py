"""
This question was asked by Google.

Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
"""
from random import randint


def get_random_number(n, integers):
    num = randint(0, n - 1)
    if num in integers:
        return get_random_number(n, integers)
    else:
        return num


# Driver code
print(get_random_number(5, [1, 2]))
