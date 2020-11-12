# -*- coding: utf-8 -*-
"""
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""

class Node:
  def __init__(self, data,next=None):
      self.data = data
      self.next=next

class SinglyLinkedList:
  def __init__(self):  
    self.head = None
    self.size = 0
  
  def insert(self , val):
    self.size += 1
    newNode = Node(val)
    if self.head:
      current = self.head
      while current.next:
        current = current.next
      current.next = newNode
      
    else:
      self.head = newNode
      
      
  def remove_k_last_element(self,k):
    listSize = self.size
    current = self.head
    while current.next:
      listSize -= 1 
      if listSize == k:
        current.next = current.next.next
        break
      current = current.next

  

def displayList(node):
  if not node:
    return
  print(node.data)
  displayList(node.next)
    

if __name__ == "__main__":
  List = SinglyLinkedList()
  elementToRemove = 3
# Adding values to List
  for i in range(11):
    List.insert(i)

  displayList(List.head)
  print("\nDisplaying the list elements after removing some element:\n")
  List.remove_k_last_element(elementToRemove)
  displayList(List.head)
