def a():
    pass
def aa():
    pass
def aaa():
    pass
def aaaa():
    pass
def aaaaa():
    pass
def aaaaaa():
    pass
def aaaaaaa():
    pass
def aaaaaaaa():
    pass
def aaaaaaaaa():
    pass

n, k, d =[int(i) for i in input().split()]

# if k % 2 == 0:
#     if k % 4 == 0:
#         aaaa()
#     elif k % 6 == 0:
#         sorted(set(aa()).intersection(set(aaa())))
#     elif k % 8 == 0:
#         aaaaaaa()
#     else:
#         aa()
# elif k % 3 == 0:
#     aaa()
# elif k % 5 == 0:
#     aaa()
# elif k % 7 == 0:
#     aaa()
# elif k % 9 == 0:
#     aaa()
for i in range(10,1,-1):
    print(i)
    if k % i == 0:
        f = 'a' * i
        print(f'nums = {f}()')
        exec(f'nums = {f}()')
        break