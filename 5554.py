a = int(input())
b = int(input())
c = int(input())
d = int(input())

total_sec = a + b + c + d

result_min = total_sec // 60
result_sec = total_sec - (result_min * 60)

print(result_min)
print(result_sec)