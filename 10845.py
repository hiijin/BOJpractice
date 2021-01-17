import sys
input = sys.stdin.readline


class Queue:
    def __init__(self):
        self.data = list()

    def push(self, value):
        self.data.insert(0, value)

    def pop(self):
        try:
            return self.data.pop()
        except IndexError:
            return -1

    def size(self):
        return len(self.data)

    def front(self):
        if len(self.data) == 0:
            return -1
        else:
            return self.data[-1]

    def back(self):
        if len(self.data) == 0:
            return -1
        else:
            return self.data[0]

    def empty(self):
        if len(self.data) == 0:
            return 1
        else:
            return 0


queue = Queue()
n = int(input().strip())
for i in range(n):
    comm = input().strip().split()
    c = comm[0]

    if c == 'push':
        queue.push(int(comm[1]))
    elif c == 'pop':
        print(queue.pop())
    elif c == 'size':
        print(queue.size())
    elif c == 'empty':
        print(queue.empty())
    elif c == 'top':
        print(queue.top())
    elif c == 'front':
        print(queue.front())
    elif c == 'back':
        print(queue.back())

