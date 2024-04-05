n = int(input())
s = 0
i = 1
while i:
    guess = n-((n-s)//2)
    print(guess)
    i = int(input())
    if i == 1:
        s += (n-s)//2
    elif i == -1:
        n -= (n-s)//2