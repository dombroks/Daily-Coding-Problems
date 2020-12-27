"""
This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].

"""


def square_list(sorted_list):
    s_list = []
    for num in sorted_list:
        s_list.append(pow(num, 2))
    s_list.sort()
    return s_list


# Driver code
assert square_list([-9, -2, 0, 2, 3]) == [0, 4, 4, 9, 81]
