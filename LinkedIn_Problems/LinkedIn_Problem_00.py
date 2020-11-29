"""
This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.
"""
import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def is_valid_bst_helper(root, l, r):
    if root and r >= root.key >= l:
        return is_valid_bst_helper(root.left, l, root.key) and \
               is_valid_bst_helper(root.right, root.key, r)
    return not root


def is_valid_bst(root):
    return is_valid_bst_helper(root, -sys.maxsize, sys.maxsize)


# Driver code
a = Node(3)
b = Node(2)
c = Node(6)
d = Node(1)
e = Node(3)
f = Node(4)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
assert is_valid_bst(a)
