"""
This problem was asked by Microsoft.

Implement 3 stacks using a single list:

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass

"""


class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        if not stack_number < len(self.list):
            return
        stack = self.list[stack_number]
        if not stack:
            return
        value = stack.pop()
        return value

    def push(self, item, stack_number):
        if stack_number < len(self.list):
            stack = self.list[stack_number]
            stack.append(item)
        elif stack_number == len(self.list):
            new_stack = list()
            new_stack.append(item)
            self.list.append(new_stack)
