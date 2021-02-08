"""
This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
"""


def _is_palindrome(s):
    return s == s[::-1]


def get_palindrome_permutation(s):
    if _is_palindrome(s):
        return s
    permutation = s[1:] + s[0]
    return get_palindrome_permutation(permutation)


# Driver code
assert get_palindrome_permutation("carrace") == "racecar"
