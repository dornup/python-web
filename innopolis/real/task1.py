n, q, x = enter = [int(i) for i in input().split()]
d = {}
ans = 0

for i in range(n):
    t, m, k = enter2 = [int(i) for i in input().split()]
    if t not in d.keys():
        d[t] = m * (k / 100)
    else:
        d[t] += m * (k / 100)

pos = False
sum = 0
for i in sorted(d.values(), reverse=True):
    if i >= x:
        ans = 1
        pos = True
        break
    else:
        sum += i
        ans += 1
        if sum >= x:
            pos = True
            break

print(ans) if pos else print(-1)
