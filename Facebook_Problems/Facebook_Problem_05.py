"""
This problem was asked by Facebook.

Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. Try solving this without creating a copy of the list. How many swap or move operations do you need?
"""


def rotate_list(l, k):
    if k > len(l):
        return
    for i in range(k):
        l.append(l[i])
    for i in range(k):
        l.pop(0)
    return l


assert rotate_list([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2]
