def check(i, j):
    if i == 0:
        nums = [d[i+1][j]]
        if j > 0:
            nums.append(d[i][j-1])
        if j < M - 1:
            nums.append(d[i][j+1])
    elif i == N-1:
        nums = [d[i-1][j]]
        if j > 0:
            nums.append(d[i][j-1])
        if j < M - 1:
            nums.append(d[i][j+1])
    else:
        nums = [d[i+1][j], d[i-1][j]]
        if j > 0:
            nums.append(d[i][j-1])
        if j < M - 1:
            nums.append(d[i][j+1])

    if nums.count('1') == 2:
        return True
    return False
    # if d[i][j+1] == d[i][j-1] == d[i][j] and d[i+1][j] == d[i-1][j] == '0':
    #     return True
    # elif d[i+1][j] == d[i][j] == d[i][j+1] and d[i][j-1] == d[i-1][j] == '0':
    #     return True
    #
    # elif d[i-1][j] == d[i][j] == d[i+1][j] and d[i][j+1] == d[i][j-1] == '0':
    #     return True
    # elif d[i+1][j] == d[i][j] == d[i][j-1] and d[i][j+1] == d[i-1][j] == '0':
    #     return True
    # elif d[i-1][j] == d[i][j] == d[i][j+1] and d[i+1][j] == d[i][j-1] == '0':
    #     return True
    # elif d[i+1][j] == d[i][j] == d[i][j-1] and d[i-1][j] == d[i][j+1] == '0':
    #     return True
    # return False


def go():
    for i in d:
        for j, k in enumerate(d[i]):
            if k == '1':
                if not check(i, j):
                    return False
    return True


nums = N, M = [int(i) for i in input().split()]
d = {}
n = 0
ones = 0
for i in range(N):
    d[i] = [i for i in input()]
    ones += d[i].count('1')
    n += 1 if '1' in d[i] else 0


if ones % 2 != 0 or 2 * (N + M - 2) < ones <= 4:
    print('NO')
elif n < 3:
    print('NO')
else:
    print('YES') if go() else print('NO')
