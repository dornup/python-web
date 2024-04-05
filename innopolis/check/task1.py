a, b = int(input()), int(input())
ans = 0

if a % 2 == 0 and b % 2 == 0:
    for i in range(a+2, b, 1):
        if b % i == 0 and i % a == 0:
            ans = i
            print(ans)
            break
elif a % 2 == b % 2:
    for i in range(a+1, b, 1):
        if b % i == 0 and i % a == 0:
            ans = i
            print(ans)
            break
elif b % a == 0:
    for i in range(a+1, b):
        if b % i == 0 and i % a == 0:
            ans = i
            print(ans)
            break

if not ans:
    print(-1)


# for i in nums:
#     if b % i == 0 and i % a == 0:
#         ans = i
#         print(ans)
#         break
# if not ans:
#     print(-1)