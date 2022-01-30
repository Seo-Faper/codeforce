# SET : 
'''
    [0,10,1,100,10]
    [1,2] = 1
    [1,3] = 100
    [2,4] = 10
    [3,4] = 10

'''
import sys
INF = sys.maxsize
def Floyd_Warshall():
    dist = [[INF]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = G[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j] 
    return dist

n = 5
G = [[INF for _ in range(n)] for _ in range(n)]
for i in range(1,n):
    G[i][i] = 0

G[1][2] = 1
G[1][3] = 100
G[2][3] = 100
G[3][4] = 10

dist = Floyd_Warshall()

for i in range(n):
    for j in range(n):
        print(dist[i][j],end=' ')
    print()
