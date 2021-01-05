import sys
input = sys.stdin.readline

n = int(input().strip())

p = list(map(int, input().split()))
p.sort()

sum = 0
result = 0

for i in range(n):
    sum = sum + p[i]
    result = result + sum

print(result)