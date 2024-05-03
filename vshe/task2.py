def check(i_d, j_d):
    i, j = i_d, j_d
    a = 1
    b = 1
    rectangle = []
    while j <= m-2:
        j += 1
        next_gor = d[i][j]
        if next_gor == '#':
            a += 1
        else:
            break
    while i <= n-2:
        i += 1
        next_ver = d[i][j_d]
        if next_ver == '#':
            b += 1
        else:
            break
    d_or = {}
    d_rect = {}
    d_rect[0] = ['.' for i in range(a+2)]
    if i_d == 0:
        d_or[0] = ['.' for i in range(a+2)]
    # elif j_d + a == n:
    #     d_or[0] = ['.'] + [i for i in d[i_d-1][j_d:]] + ['.']
    else:
        d_or[0] = ['.'] + [i for i in d[i_d-1][j_d:j_d+a % m]] + ['.']
    i_dict = 1
    for l in range(i_d, i_d + b):
        before = '.' if j_d == 0 else d[l][j_d-1]
        after = '.' if j_d + a == m else d[l][j_d + a]
        d_or[i_dict] = [before] + [i for i in d[l][j_d:]] + [after]
        d_or[i_dict] = d_or[i_dict] if a == m else d_or[i_dict][:a+1] +[after]
        d_rect[i_dict] = ['.'] + ['#']*a + ['.']
        i_dict += 1
    d_rect[i_dict] = ['.' for i in range(a+2)]
    if i_d+b == n:
        d_or[i_dict] = ['.' for i in range(a+2)]
    else:
        d_or[i_dict] = ['.'] + [i for i in d[i_d+b%n][j_d:j_d+a%m]] + ['.']
    # print(i_d, j_d, b, a)
    for i  in range(i_d, i_d + b):
        for j in range(j_d, j_d + a):
            rectangle.append([i,j])
    # print(d[i_d], d_or, d_rect)
    return rectangle, d_or == d_rect

def go():
    for i in d:
        for j, k in enumerate(d[i]):
            if k == '#' and not ([i,j] in rect[len(rect)-1] or [i, j] in not_rect[len(not_rect)-1]):
                r = check(i, j)
                if r[1]:
                    # print(r)
                    rect.append(r[0])
                else:
                    not_rect.append(r[0])

    return rect

n, m = [int(i) for i in input().split()]
d = {}
rect = [[]]
not_rect=[[]]
for i in range(n):
    d[i] = [i for i in input()]

go()
print(len(rect)-1)
