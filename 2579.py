import sys
input = sys.stdin.readline

n = int(input().strip())
score = []
arr = []

for i in range(n):
    score.append(int(input().strip()))

arr.append(score[0])
if n == 1:
    print(arr[n-1])
    quit()

arr.append(max(score[0] + score[1], score[1]))
if n == 2:
    print(arr[n-1])
    quit()

arr.append(max(score[0] + score[2], score[1] + score[2]))
if n == 3:
    print(arr[n-1])
    quit()

for i in range(3, n):
    arr.append(max(arr[i-3] + score[i-1] + score[i], arr[i-2] + score[i]))

print(arr[n-1])

