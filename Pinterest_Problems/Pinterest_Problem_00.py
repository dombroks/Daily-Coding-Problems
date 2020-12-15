"""
This problem was asked by Pinterest.

Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""


def is_last_reachable_helper(arr, start_index, target_index):
    if start_index == target_index:
        return True

    hop = arr[start_index]
    if not hop or (start_index + hop > target_index):
        return False

    return is_last_reachable_helper(arr, start_index + hop, target_index)


def is_last_reachable(arr):
    return is_last_reachable_helper(arr, 0, len(arr) - 1)


assert is_last_reachable([2, 0, 1, 0])
assert not is_last_reachable([1, 1, 0, 1])
assert not is_last_reachable([2, 1])
