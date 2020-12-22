"""
This problem was asked by Google.

Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?

"""


def reverse_string(string):
    return " ".join(reversed(string.split(" ")))


assert reverse_string("hello world here") == "here world hello"
