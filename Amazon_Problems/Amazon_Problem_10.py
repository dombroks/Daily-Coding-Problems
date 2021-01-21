"""
This problem was asked by Amazon.

Given a pivot x, and a list lst, partition the list into three parts.

    The first part contains all elements in lst that are less than x
    The second part contains all elements in lst that are equal to x
    The third part contains all elements in lst that are larger than x

Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].

"""


def get_partition(x, lst):
    less_than_x_lst = list()
    equal_to_x_lst = list()
    more_than_x_lst = list()
    for num in lst:
        if num < x:
            less_than_x_lst.append(num)
        elif num == x:
            equal_to_x_lst.append(num)
        else:
            more_than_x_lst.append(num)

    return less_than_x_lst + equal_to_x_lst + more_than_x_lst


# Driver code
lst = [9, 12, 3, 5, 14, 10, 10]
x = 10
print(get_partition(x, lst))
