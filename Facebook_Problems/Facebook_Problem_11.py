"""
This problem was asked by Facebook.

Given a binary tree, return the level of the tree with minimum sum.

"""

import sys


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_maxsum_level_helper(level, nodes, parent_sum):
    child_nodes = list()
    nodes_sum = 0
    for node in nodes:
        nodes_sum += node.val
        if node.left:
            child_nodes.append(node.left)
        if node.right:
            child_nodes.append(node.right)

    max_sum = max(nodes_sum, parent_sum)
    if child_nodes:
        max_sum = get_maxsum_level_helper(level + 1, child_nodes, max_sum)

    return max_sum


def get_maxsum_level(root):
    max_sum = get_maxsum_level_helper(0, [root], -sys.maxsize)
    return max_sum


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(get_maxsum_level(root))
