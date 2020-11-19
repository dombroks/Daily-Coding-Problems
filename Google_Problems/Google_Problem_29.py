"""
This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

    def __repr__(self):
        return str(self.val)


def get_deepest_node_helper(root, depth):
    if not root.right and not root.left:
        return root, depth

    left_depth = depth
    right_depth = depth
    if root.left:
        left_deepest, left_depth = get_deepest_node_helper(root.left, depth + 1)
    if root.right:
        right_deepest, right_depth = get_deepest_node_helper(root.right, depth + 1)

    return (left_deepest, left_depth) if left_depth > right_depth \
        else (right_deepest, right_depth)


def get_deepest_node(root):
    return get_deepest_node_helper(root, 0)[0]


if __name__ == "__main__":
    root = Node("a", Node("b", Node("d")), Node("c"))
    node = get_deepest_node(root)
    assert node.val == 'd'
