import sys
input = sys.stdin.readline

arr = []
n = int(input().strip())
for i in range(n):
    arr.append(int(input().strip()))

arr.sort()

cnt = 1
start = 0
max_cnt = 1

for i in range(1, n):
    cnt += 1
    while arr[i] - arr[start] > 4:
        start += 1
        cnt -= 1
    max_cnt = max(max_cnt, cnt)

if max_cnt > 5:
    max_cnt = 5

print(5 - max_cnt)