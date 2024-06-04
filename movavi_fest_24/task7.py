n = int(input())
nums = [i for i in input().split(' ')]
d = {}
for i, e in enumerate(nums):
    if int(e) % 2 == 0:
        d[e] = i
nums = [i for i in nums if i not in d.keys()]
nums = sorted(nums)
for i in d.keys():
    nums.insert(d[i], i)

print(' '.join(nums))