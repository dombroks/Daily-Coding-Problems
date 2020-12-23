"""
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:
"""

class Node():
  def __init__(self,val,left=None,right=None):
    self.val=val
    self.left=left
    self.right=right


def evaluate_tree(root):
  if root.val.isnumeric():
    return int(root.val)
  
  return eval("{} {} {}".format(evaluate_tree(root.left), root.val, evaluate_tree(root.right)))

# Driver code
if __name__ == "__main__":
 root = Node('*')
 root.left= Node('+')
 root.right=Node('+')
 root.left.left = Node("3")
 root.left.right = Node("2")
 root.right.right = Node("5")
 root.right.left = Node("4")

 print(evaluate_tree(root))
