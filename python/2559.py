N,K = map(int,input().split())
L = list(map(int,input().split()))

result = 0
for i in range(K):
    result +=L[i]

ans = result
for i in range(K,N):
    result -= L[i-K]
    result += L[i]
    ans = max(ans,result)
print(ans)
