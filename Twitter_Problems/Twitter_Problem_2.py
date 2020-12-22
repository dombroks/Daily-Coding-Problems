"""
This problem was asked by Twitter.

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
"""
import collections


class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None


parents = []


def get_lowest_common_ancestor(root_val, node1, node2):
    get_parent(node1)
    get_parent(node2)

    p_list = [item for item, count in collections.Counter(parents).items() if count > 1]
    if len(p_list) == 1:
        return root_val
    if len(p_list) == 2:
        p_list.remove(root_val)
        return p_list[0]


def get_parent(node):
    if node is None:
        return
    parents.append(node.val)
    return get_parent(node.parent)


a1 = Node(40)
a2 = Node(20)
a3 = Node(60)
a4 = Node(10)
a5 = Node(30)
a6 = Node(50)
a7 = Node(70)

a2.parent = a1
a3.parent = a1
a4.parent = a2
a5.parent = a2
a6.parent = a3
a7.parent = a3

assert get_lowest_common_ancestor(a1.val, a6, a1) == 40
