N,M = map(int, input().split())
l = [int(input()) for _ in range(M)]
l.sort()
ans = 0
p = 0
for i in range(len(l)):
    egg = min((M-i),N)*l[i]
    if ans < egg:
        ans = egg
        p = l[i]
print(p,ans)
