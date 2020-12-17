
"""
This problem was asked by Amazon.

Implement a stack that has the following methods:

    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
    max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
"""

class Stack:
  def __init__(self):
      self.list=[]


  def push(self,val):
    self.list.append(val)
  
  def pop(self):
    if len(self.list)==0 :
      return None
    else:
      self.list.pop()
  
  def max(self):
    if len(self.list)==0 :
      return None
    else:
      return max(self.list)
  
  def display(self):
    for e in self.list:
      print(e)
    
# Driver code
stack = Stack()

# Pushing new elements to stack
for i in range(6):
  stack.push(i)

print("Stack elements: ")
stack.display()

print("After pop operation: ")
stack.pop()
stack.display()

assert stack.max() == 4
