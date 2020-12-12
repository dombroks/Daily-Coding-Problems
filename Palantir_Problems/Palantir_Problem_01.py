"""
This problem was asked by Palantir.

Given a number represented by a list of digits, find the next greater permutation of a number, in terms of lexicographic ordering. If there is not greater permutation possible, return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3]. The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding the input memory)?
"""


def get_greater_permutation(arr):
    if len(arr) < 2:
        return

    for index in range(len(arr) - 1, -1, -1):
        if index > 0 and arr[index - 1] < arr[index]:
            break

    if index == 0:
        arr.reverse()
    else:
        for k in range(len(arr) - 1, index - 1, -1):
            if arr[k] > arr[index - 1]:
                tmp = arr[k]
                arr[k] = arr[index - 1]
                arr[index - 1] = tmp
                break

        sub_array = arr[index:]
        sub_array.reverse()
        arr[index:] = sub_array

    return arr


assert get_greater_permutation([1, 2, 3]) == [1, 3, 2]
