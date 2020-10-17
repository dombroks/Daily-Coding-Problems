# -*- coding: utf-8 -*-
"""
This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
"""

class Node:
  def __init__(self,val,left=None,right=None):
    self.val = val 
    self.left=left
    self.right=right
  

def build_tree(preorder,inorder):
  if not preorder or not inorder:
    return None
  
  root_val = preorder[0]
  if len(preorder) == 1:
      return Node(root_val)

  root_node = Node(root_val)
  
  
  for i , val in enumerate(inorder):
    if val == root_node.val :
      root_node.left = build_tree(preorder[1:i+1],inorder[:i])
      root_node.right = build_tree(preorder[i+1:],inorder[i+1:])
  return root_node

tree = build_tree(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                  ['d', 'b', 'e', 'a', 'f', 'c', 'g'])

assert tree.val == 'a'
assert tree.right.val == 'c'
assert tree.left.left.val == 'd'
assert tree.right.left.val == 'f'
assert tree.right.right.val == 'g'
