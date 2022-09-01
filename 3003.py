# 1 1 2 2 2 8
# 
L = [1,1,2,2,2,8]
ans = []
R = list(map(int,input().split()))
for i in range(len(R)):
    ans.append(L[i] - R[i])

print(*ans)