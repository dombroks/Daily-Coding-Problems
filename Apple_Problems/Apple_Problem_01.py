# -*- coding: utf-8 -*-
"""
This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.
"""

class Stack:
  def __init__(self):
    self.list = []
  
  def push(self,value):
    self.list.append(value)

  def pop(self):
    return self.list.pop()

  
class Queue:
  def __init__(self):
    self.master_stack = Stack()
    self.helper_stack = Stack()

  def __repr__(self):
        return str(self.main_stack)
  
  def enqueue(self,value):
    self.master_stack.push(value)

  def dequeue(self):
    if not self.master_stack:
      return None
    
    while self.master_stack.list:
          self.helper_stack.push(self.master_stack.pop())
    val = self.helper_stack.pop()
    while self.helper_stack.list:
        self.master_stack.push(self.helper_stack.pop())
    return val

# Driver code
q = Queue()
for i in range(5):
  q.enqueue(i)
assert q.master_stack.list == [0,1,2,3,4]
q.enqueue(5)
assert q.master_stack.list == [0,1,2,3,4,5]
val = q.dequeue()
assert val == 0
