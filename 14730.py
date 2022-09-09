n = int(input())
ans = 0
for i in range(n):
    a,b = map(int, input().split())
    if b!=0:
        ans +=a*b*1**(b-1)

print(ans)