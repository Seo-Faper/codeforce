n, x, k = map(int, input().split())
l = [0]*(n+1)
l[x] = 1
for i in range(k):
    a, b = map(int,input().split())
    tmp = l[a]
    l[a] = l[b]
    l[b] = tmp

print(l.index(1))