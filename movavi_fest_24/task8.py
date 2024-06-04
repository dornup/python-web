x_o, y_o = [int(i) for i in input().split(' ')]
r = int(input())
x, y = [int(i) for i in input().split(' ')]

l = ((x-x_o)**2 + (y-y_o)**2)**0.5
print('YES' if l <= r else 'NO')