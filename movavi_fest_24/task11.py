def pol(s):
    func = ''
    i = 0
    while s[i] != ' ':
        func += s[i]
        i += 1
    i += 1
    el1 = ''
    while s[i] != ' ':
        el1 += s[i]
        i += 1
    el2 = s[i:]
    oper = '+-/*'
    elems = el1, el2
    for i in range(len(elems)):
        for k in oper:
            if k in elems[i]:
               el = elems.pop(i)
               elems.insert(i, pol(el))
    return d[func](int(elems[0]), int(elems[1]))
    

d = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
    '//': lambda x, y: x//y
}

s = input()

print(pol(s))