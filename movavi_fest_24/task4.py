n = int(input())
nums = [int(i) for i in input().split(' ')]
res = 'YES'
for i, e in enumerate(sorted(nums)):
    if i > 1 and e != nums[i-1] + nums[i-2]:
        res = 'NO'
print(res)