"""
This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


nodes = []


def print_tree_elements_helper(root):
    if root.left is None or root.right is None:
        return

    nodes.append(root.left.val)
    nodes.append(root.right.val)
    print_tree_elements_helper(root.right)
    print_tree_elements_helper(root.left)


def print_tree_elements(root):
    nodes.append(root.val)
    print_tree_elements_helper(root)
    print(nodes)


# Driver code
r = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_tree_elements(r)
