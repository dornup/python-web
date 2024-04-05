nums = N, M = [int(i) for i in input().split()]
names = [input().lower() for i in range(N)]
text = input().split()
for i in text:
    if i.rstrip('.,') in names:
        text.insert(text.index(i), i.capitalize())
        text.remove(i)

print(' '.join(text))
