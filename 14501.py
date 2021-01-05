import sys
input = sys.stdin.readline

n = int(input().strip())

ti, pi = [], []
dp = [0] * (n + 1)

for i in range(n):
    t, p = map(int, input().split())
    ti.append(t)
    pi.append(p)

maxvalue = 0

for i in range(n):
    maxvalue = max(maxvalue, dp[i])
    if i + ti[i] > n:
        continue
    dp[i + ti[i]] = max(maxvalue+pi[i], dp[i+ti[i]])

print(max(dp))