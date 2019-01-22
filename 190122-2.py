class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) -1
        return self.items[last]

    def size(self):
        return len(self.items)

stack = Stack()

for c in "yesterday":
    stack.push(c)
print(stack.items)

text = ""
while not stack.is_empty():
    text += stack.pop()
print(text)

