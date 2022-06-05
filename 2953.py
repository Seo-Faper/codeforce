ans = []
for i in range(5):
    L = list(map(int,input().split()))
    ans.append(sum(L))

print(ans.index(max(ans))+1,max(ans))