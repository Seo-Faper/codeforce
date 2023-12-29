N = int(input())
L = [list(map(int,input().split()))for _ in range(N)]
result = [[0 for _ in range(N)] for _ in range(N)]
for m in range(5):
    for i in range(N):
    #    print(L[m][i],end='|')
        for j in range(i+1,N):
            if L[i][m] ==L[j][m]:
                result[j][i] = 1
                result[i][j] = 1
    #    print("")
 #   print("----")

#print(result)
ans = []
for i in result:
    ans.append(i.count(1))
print(ans.index(max(ans))+1)