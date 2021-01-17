import sys

input = sys.stdin.readline


class Stack:
    def __init__(self):
        self.data = list()

    def push(self, value):
        self.data.append(value)

    def pop(self):
        try:
            return self.data.pop()
        except IndexError:
            return -1

    def empty(self):
        if len(self.data) == 0:
            return 1
        else:
            return 0

    def top(self):
        try:
            return self.data[len(self.data) - 1]
        except IndexError:
            return -1


n = int(input().strip())
num = []
result = []
stack = Stack()

for i in range(n):
    num.append(int(input().strip()))

num_index = 0

for i in range(1, n+1):
    stack.push(i)
    result.append('+')
    while True:
        if stack.top() == num[num_index]:
            stack.pop()
            result.append('-')
            num_index += 1
            if num_index >= n:
                break
        else:
            break

if not stack.empty():
    print("NO")
else:
    for r in result:
        print(r)

