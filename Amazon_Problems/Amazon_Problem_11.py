import sys
from heapq import heappop, heappush


class Stack:
    def __int__(self):
        self.counter = sys.maxsize
        self.stack = list()

    def push(self, item):
        heappush(self.stack, (self.counter, item))
        self.counter -= 1

    def pop(self):
        if not self.stack:
            return None

        _, item = heappop(self.stack)
        return item


# Driver code
stk = Stack()
for i in range(10):
    stk.push(i)


