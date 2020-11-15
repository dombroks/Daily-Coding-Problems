"""
This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
"""
cache = None


def get_subsequence(arr, start):
    if start == len(arr):
        return 0

    current = arr[start]
    length = 1
    for index in range(start + 1, len(arr)):
        if arr[index] >= current:
            if index in cache:
                count = cache[index]
            else:
                count = get_subsequence(arr, index) + 1
                cache[index] = count
            if count > length:
                length = count

    return length


def get_subsequence_helper(arr):
    global cache
    cache = dict()
    return get_subsequence(arr, 0)


assert get_subsequence_helper([]) == 0
assert get_subsequence_helper([0, 1]) == 2
assert get_subsequence_helper([0, 2, 1]) == 2
assert get_subsequence_helper([0, 1, 2]) == 3
assert get_subsequence_helper([2, 1, 0]) == 1
assert get_subsequence_helper(
    [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6
