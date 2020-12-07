import sys
input = sys.stdin.readline


class Stack:
    def __init__(self):
        self.data = list()

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.data.pop(-1)

    def size(self):
        return len(self.data)

    def empty(self):
        if len(self.data) == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.empty():
            return -1
        else:
            return self.data[len(self.data) - 1]


n = int(input())
stack = Stack()

for i in range(n):
    comm = input().strip().split()
    c = comm[0]

    if c == 'push':
        stack.push(int(comm[1]))
    elif c == 'pop':
        print(stack.pop())
    elif c == 'size':
        print(stack.size())
    elif c == 'empty':
        print(stack.empty())
    elif c == 'top':
        print(stack.top())
