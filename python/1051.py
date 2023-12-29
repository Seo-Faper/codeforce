N,M = map(int,input().split())
L = [list(map(int,list(input()))) for _ in range(N)]
#print(L)
def find_max(x,y):
    nx = N-x
    ny = M-y
    start = L[x][y]
    q = 1
   # print(f"nx: {nx} ny:{ny}")
    for i in range(min(nx,ny)):
        if L[x][y+i] == start and L[x+i][y] == start and L[x+i][y+i]==start:
            q = i
   #     print(f"i:{i} L[x][y]:{L[x][y]}")
    return q
ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans,find_max(i, j)+1)
        #print(find_max(i,j))
print(ans**2)