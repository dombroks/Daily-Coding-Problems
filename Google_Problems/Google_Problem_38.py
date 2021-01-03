"""
This problem was asked by Google.

Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15

Return the nodes 5 and 15.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


nodes = []


def get_nodes(root):
    if not root:
        return
    nodes.append(root.val)
    get_nodes(root.left)
    get_nodes(root.right)


def nodes_sum(root, k):
    get_nodes(root)
    for i in range(len(nodes)):
        node = nodes[i]
        for j in range(i + 1, len(nodes)):
            if node + nodes[j] == k:
                return node, nodes[j]

    return None


# Driver code
ROOT = Node(10, Node(5), Node(15, Node(11), Node(15)))
print(nodes_sum(ROOT, 20))
