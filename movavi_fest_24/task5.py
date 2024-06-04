n, m = [int(i) for i in input().split(' ')]
num = [i for i in range(m+1, n, -1)]
nums = list(map(lambda x: [sum([int(i) for i in str(x)[::2]]), sum([int(i) for i in str(x)[1::2]])], num))
for i in nums:
    if len(set(i)) == 1:
        print(num[nums.index(i)])
        break