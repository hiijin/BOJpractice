import sys
input = sys.stdin.readline


def isVPS(lst):
    stack = []

    for i in range(len(lst)):
        stack.append(lst[i])

        if lst[i] == ')':
            if len(stack) >= 2:
                stack.pop()
                stack.pop()
            else:
                return 'NO'

    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


n = int(input().strip())
lst = []

for i in range(n):
    s = input().strip()
    lst = list(s)
    print(isVPS(lst))

