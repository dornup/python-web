def game(d):
    d[start_x].replace(d[start_x][start_y], '2')
    exec(f'{direction}(d, start_x, start_y)')


def u(d, start_x, start_y):
    while start_x >= 0:
        start_x-=1
        d[start_x].replace(d[start_x][start_y], '2')
    if


nums = N, M = [int(i) for i in input().split()]
d = {}

for i in range(N):
    d[i] = input()

pos = start_x, start_y, direction = [i for i in input().split()]
start_x, start_y = int(start_x), int(start_y)
game(d)
