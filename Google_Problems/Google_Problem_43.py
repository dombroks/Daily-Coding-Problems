"""
This problem was asked by Google.

Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""


def get_first_recurring_char(sequence):
    for i in range(len(sequence) - 1):
        current = sequence[i]
        next = sequence[i + 1]
        if current == next:
            return current

    return None


# Driver code
assert get_first_recurring_char("acbbac") == "b"
assert not get_first_recurring_char("abcdef")
