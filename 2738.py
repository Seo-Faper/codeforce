'''

3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100

'''

N,M = map(int,input().split())
L = [list(map(int, input().split())) for _ in range(N)]
R = [list(map(int, input().split())) for _ in range(N)]

#print(L,R)

for i in range(N):
    for j in range(M):
        L[i][j] += R[i][j]
        print(L[i][j],end=' ')
    print()