import sys
input = sys.stdin.readline

n = int(input().strip())

testcase = []

for _ in range(n):
    testcase.append(int(input().strip()))

dp = [0, 1, 2, 4]
for i in range(4, 11):
    dp.append(sum(dp[-3:]))

for i in range(n):
    print(dp[testcase[i]])

