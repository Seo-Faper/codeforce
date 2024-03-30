import sys
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

prefix = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + graph[i][j]

for i in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    answer = prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1]
    sys.stdout.write(str(answer)+"\n")