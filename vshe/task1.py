# я люблю питон, ААААААААААААААААААААААААААААААААААААААААААААААААААААА
import sys
sys.set_int_max_str_digits(0)

n, k, d =[int(i) for i in input().split()]

d -= 1
nums = [int(str(n)+str(i)) for i in range(10)]
num = -1
for i in nums:
    if i % k == 0:
        n = i
        num = int(str(n)+'0'*d)
        break
print(num)