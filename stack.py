import sys
input=sys.stdin.readline

class Stack:
    items = []
    def __init__(self):
        return
    def push(self, item):
        self.items.append(item)
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return -1
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return -1
    def is_empty(self):
        if self.items:
            return 0
        else:
            return 1

N = int(input())
stack = Stack()
for i in range(N):
    a = input().split()
    if "push" == a[0]:
        stack.push(int(a[1]))
    elif "pop" in a[0]:
        print(stack.pop())
    elif "top" in a[0]:
        print(stack.peek())
    elif "size" in a[0]:
        print(len(stack.items))
    elif "empty" in a[0]:
        print(stack.is_empty())
    
