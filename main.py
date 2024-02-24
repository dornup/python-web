def solve(n, t, views):
    fin_views = []
    a = []
    d = {}
    for i in range(t):
        if views[i+1:].count(views[i])==1:
            fin_views.append(views[i])
    for i in fin_views:
        watch = views.count(i)
        a.append(watch)
    for watch in a:
        m = a[0]
        if watch > a[0]:
            fin_views.insert(0, fin_views[a.index(watch)])
            a.insert(0, watch)
    for i, j in enumerate(a):
        return fin_views[j], i

n, t = list(map(int, input().split()))
views = list(map(int, input().split()))

print(solve(n, t, views))