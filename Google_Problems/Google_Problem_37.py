"""
This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""


def can_be_shifted(string_a, string_b):
    before_shifting = string_a
    for i in range(len(string_a)):
        string_a = string_a[-1:] + string_a[:-1]
        if string_a == string_b:
            return True
        if string_a == before_shifting:
            break

    return False


assert not can_be_shifted("abc", "acb")
assert can_be_shifted("abcde", "cdeab")
