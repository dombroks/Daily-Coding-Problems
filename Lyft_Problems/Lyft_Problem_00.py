"""
This problem was asked by Lyft.

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""

def sum_to_k(integers, k):
    global elements
    for i in range(len(integers)):
        elements = []
        temp = integers[i]
        elements.append(temp)
        for j in range(i + 1, len(integers)):
            if sum(elements) < k:
                elements.append(integers[j])
        if sum(elements) == k:
            break

    return elements


print(sum_to_k([1, 2, 3, 4, 5], 9))
