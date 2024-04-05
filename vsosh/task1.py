start = [i for i in input().split(':')]
hours = int(start[0].lstrip('0'))
seconds = start[1]
if seconds[0] == '0':
    seconds = int(seconds[1])
else:
    seconds = int(seconds)

test = int(input())

microseconds_from_start = (hours - 8) * 3600000000 + seconds * 60000000
print(microseconds_from_start // test)
