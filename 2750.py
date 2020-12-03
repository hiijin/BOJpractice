n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

# nums.sort()

for i in range(n):
    for j in range(n-1-i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

for i in range(n):
    print(nums[i])
