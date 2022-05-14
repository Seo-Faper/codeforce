N, M = map(int,input().split())
ans = 0
S = []

for i in range(N):
    S.append(input())

for i in range(M):
    k = input()
    if k in S: ans+=1

print(ans)