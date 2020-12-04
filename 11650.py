n = int(input())
c = []

for i in range(n):
    a, b = map(int, input().split(" "))
    lst = [a, b]
    c.append(lst)

# 시간초과
# for i in range(n):
#     for j in range(n - 1 - i):
#         if c[j][0] > c[j+1][0]:
#             c[j], c[j+1] = c[j+1], c[j]
#         if c[j][0] == c[j+1][0]:
#             if c[j][1] > c[j+1][1]:
#                 c[j], c[j+1] = c[j+1], c[j]


for i in range(0, n):
    print(c[i][0], c[i][1])
