"""
This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f

should become:

  a
 / \
 c  b
 \  / \
  f e  d

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def display_tree(root):
    if not root:
        return
    print(root.val)
    display_tree(root.left)
    display_tree(root.right)


def invert_tree(root):
    if not root.right or not root.left:
        return
    new_right, new_left = root.left, root.right
    root.left = new_left
    root.right = new_right
    invert_tree(root.left)
    invert_tree(root.right)


# Driver code
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

display_tree(a)
invert_tree(a)
print("After inverting")
display_tree(a)
