n = int(input())
L = list(map(int, input().split()))
v = int(input())
ans = 0
for i in L:
    if i == v: ans+=1

print(ans)