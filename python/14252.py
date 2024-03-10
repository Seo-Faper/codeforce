import math
n = int(input())
l = list(map(int,input().split()))
ans = 0
l.sort()
for i in range(1,n):
    if math.gcd(l[i-1],l[i]) == 1:
        continue
    for j in range(l[i-1],l[i]+1): # 17 42
        if math.gcd(l[i-1],j) == 1 and math.gcd(l[i],j) == 1:
            ans+=1
            break
        if j == l[i]:
            ans+=2
print(ans)