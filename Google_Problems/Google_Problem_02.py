# -*- coding: utf-8 -*-
"""Google_Problem_03


This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""

# node structure.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def serialize(node,result) :
  if node != None:
    result.append(node.val) 
    serialize(node.left,result)
    serialize(node.right,result)

  else:
    result .append('/') 
  
# def deserialize(result):
 
  
 
 
if __name__ == "__main__":
  node = Node('root', Node('left', Node('left.left')), Node('right'))
  serial = []
  serialize(node,serial)
  ser = "".join(serial)
 
  print(ser)
