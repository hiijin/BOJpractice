n, l, w, h = map(int, input().split())

start = 0.0
stop = 0.0

stop = max(l, w, h)

for i in range(0, 10000):
    mid = float((start + stop) / 2)
    if (l / mid) * (w / mid) * (h / mid) >= n:
        start = mid
    else:
        stop = mid

print('%.1f' % stop)
