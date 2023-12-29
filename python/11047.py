N,K = map(int,input().split())
L = [int(input()) for _ in range(N)]

t  = K
ans = 0
for i in reversed(L):
    if K >= i:
        ans += K // i
        K %= i
    elif K == 0:
        break

print(ans)