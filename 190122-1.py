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
l = [1,2,3,4,5]

for n in l:
    stack.push(n)

l2 = []
while not stack.is_empty():
    l2.append(stack.pop())
print(l2)

