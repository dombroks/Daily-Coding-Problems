"""
This problem was asked by Google.

Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def is_palindrome(contents):
    return contents == contents[::-1]


# sll = singly linked list
def get_sll_elements(head):
    elements = []
    curr = head
    while curr:
        elements.append(curr.val)
        curr = curr.next
    return elements


# Driver code
a0 = Node('a')
a1 = Node('a')
b0 = Node('b')
c0 = Node('c')

a0.next = b0
b0.next = c0

assert not is_palindrome(get_sll_elements(a0))
b0.next = a1
assert is_palindrome(get_sll_elements(a0))
