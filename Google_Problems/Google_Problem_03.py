# -*- coding: utf-8 -*-
"""

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 
 Note : This solution is provided by Daily-Coding-Problem website , you just need to search about the problem, I just made the Node structure and the main.
"""

# node structure.
class Node:
    def __init__(self, val,left=None,right=None):
        self.val = val
        self.left = left
        self.right= right

def is_unival(root):
    return unival_helper(root, root.val)

def unival_helper(root, value):
    if root is None:
        return True
    if root.val == value:
        return unival_helper(root.left, value) and unival_helper(root.right, value)
    return False

def count_unival_subtrees(root):
    if root is None:
        return 0
    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)
    return 1 + left + right if is_unival(root) else left + right
 

if __name__ == "__main__":
  node = Node(0, Node(1), Node(0,Node(1,Node(1),Node(1)),Node(0)))
  print( count_unival_subtrees(node))
