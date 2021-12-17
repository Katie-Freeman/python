class Stack:
    def __init__(self):
        self.items = []

    def push (self, item):
        if item is not None:
            self.items.append(item)

    def pop (self):
        if len(self.items) > 0:
            item = self.items[-1]
            del self.items[-1]
            return item
        else:
            return None

stack = Stack()
stack.push(3)
stack.push(10)
stack.push(20)
stack.push(2)
stack.push(1)
print(stack.__dict__)
print("pop")
print(stack.pop())
print(stack.pop())
print(stack.pop())

