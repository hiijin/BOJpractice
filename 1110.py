n = int(input())

num = n
cnt = 0

while True:
    one = num % 10
    ten = num // 10
    num = one * 10 + ((one + ten) % 10)
    cnt += 1

    if num == n:
        print(cnt)
        break

