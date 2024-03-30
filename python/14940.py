import sys
input = sys.stdin.readline
from collections import deque
def bfs(i,j):
    Q = deque([(i,j)])
    dir = [(-1,0),(1,0),(0,-1),(0,1)]
    visit[i][j] = 0
    while Q:
        x,y = Q.popleft()
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if not (0 <= nx < N and 0 <= ny < M and visit[nx][ny] == -1):
                continue
            if board[nx][ny] == 0:
                visit[nx][ny] = 0
            elif board[nx][ny] == 1:
                visit[nx][ny] = visit[x][y] + 1
                Q.append([nx, ny])
    
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visit = [[-1] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 2 and visit[i][j] == -1:
            bfs(i,j)
for i in range(N):
    for j in range(M):
            if board[i][j] == 0: print(0,end=' ')
            else:
                print(visit[i][j], end=' ')
    print()