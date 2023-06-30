from collections import deque

class Stack:
    def __init__(self):
        self.queue = deque()

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        if not self.is_empty():
            return self.queue.pop()
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

stack = Stack()

stack.push(1)
stack.push(2)
print(stack.pop())
stack.push(3)
print(stack.pop())
print(stack.pop())
