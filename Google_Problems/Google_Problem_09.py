# -*- coding: utf-8 -*-
"""
This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

    is_locked, which returns whether the node is locked
    lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
    unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes.
"""

class Node:
  def __init__(self, val,parent,left=None,right=None):
      self.val = val
      self.left = left
      self.right = right
      self.parent= parent
      self.isLocked= False

  def is_locked(self):
    return self.isLocked
  
  def lock(self):
    if (is_parent_locked(self) or is_left_or_right_locked(self)):
      print("You can't lock this node")
      return False
    else:
      print("The node has been locked")
      self.isLocked = True
      return True
  
  def unlock(self):
    if self.is_locked():
      print("The node has been unlocked")
      self.isLocked = False
      return True
    else:
      print("You can't unlock this node")
      return False

def is_left_or_right_locked(node):
  if not node:
    return False
  return is_left_or_right_locked(node.right) and is_parent_locked(node.left)

def is_parent_locked(node):
    if not node:
      return
    if not node.parent:
      return False

    if node.parent.isLocked:
      return True
    
    return is_parent_locked(node.parent)


    

# Driver code
if __name__ == "__main__" :
  a = Node("1",None,b,c)
  b = Node ("2",a,d,e)
  c = Node ("3" , a,f,g)
  d = Node ("4",b)
  e = Node ("5" ,b)
  f = Node ("6",c)
  g = Node("7" , c)

# Testing...
# Locking the node c
  c.lock()
# Trying to lock the node g
  g.lock()
