# -*- coding: utf-8 -*-
"""
This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.
"""

class Node:
    def __init__(self, val,left=None,right=None ):
        self.val = val
        self.left = left
        self.right = right



listOfValues = []
def get_second_largest_node(node):
  
  if not node:
    return

  listOfValues.append(node.val)
  get_second_largest_node(node.left)
  get_second_largest_node(node.right)
  
  listOfValues.sort()
  return listOfValues[-2]
 


# Program
node = Node(1, Node(2, Node(3)), Node(4,Node(5,Node(6,Node(7),Node(8)))))
Head = Node(0,node)
print(get_second_largest_node(Head))
