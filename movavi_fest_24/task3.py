n = input()[2:]
nums = [i for i in n if i.isdigit()]
print('YES' if len(set(nums)) == len(nums) else 'NO')