N = int(input())
S1 = set(list(map(int,input().split())))

M = int(input())
S2 = list(map(int,input().split()))
d = dict()
ans = [0] * M
for i in range(M):
    d[S2[i]] = i


for i in S1 & set(S2): 

    ans[d[i]] = 1

for i in ans:
    print(i,end = ' ')