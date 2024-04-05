def two(i, j):
    if d[i+1][j] == d[i][j+1] == 1:
        return 1
    return 0


def chek(i, j):
    tr = 0
    right, down = m-j-1, n-i
    for o in range(1, min(right, down)+1):
        b = d[i + o][j]
        if 0 < b <= right:
            a = d[i][j + b]
            if 0 < a <= down:
                if a + b == d[i][j] and o == a:
                    tr += 1
    return tr

def minus(d):
    for i in d:
        for j, item in enumerate(d[i]):
            d[i].pop(j)
            d[i].insert(j, item-1)
    return d

def plus(d):
    for i in d:
        for j, item in enumerate(d[i]):
            d[i].pop(j)
            d[i].insert(j, item+1)
    return d



n, m = enter = [int(i) for i in input().split()]
d = {}
twos = True
triangles = 0
for i in range(1, n+1):
    d[i] = [int(j) for j in input().split()]
    for j in d[i]:
        if j > 2:
            twos = False


while not twos:
    d = minus(d)
    checker = 1
    for i in d:
        for j in d[i]:
            if j > 2:
                twos = False
                checker = 0
        if checker:
            twos = True

g = True
trying = 0
while g:
    result = 0
    trying += 1
    for i in d:
        for j, item in enumerate(d[i]):
            if item > 1 and i < n:
                if item > 2:
                    result += chek(i, j)
                elif j < m - 1:
                    result += two(i, j)
    if result > 0 or trying == 1:
        d = plus(d)
        g = True
    else:
        g = False
    triangles += result

print(triangles)
