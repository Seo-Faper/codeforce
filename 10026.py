import sys
from collections import deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input())
board = [list(input()) for _ in range(n)]
v = [[0 for _ in range(n)] for _ in range(n)]
a,b = 0,0
dx = [-1,1,0,0] # 상하좌우 (-1,0) (1,0) (0,-1) (0,1)
dy = [0,0,-1,1]
q = deque()

def bfs(x,y):
    q.append([x,y])
    v[x][y] = cnt
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] ==board[x][y] and v[nx][ny]==0:
                    q.append([nx,ny])
                    v[nx][ny] = 1
cnt = 0
for i in range(n):
    for j in range(n):
        if v[i][j] == 0:
            bfs(i,j)
            cnt +=1
print(cnt,end=' ')

for i in range(n):
    for j in range(n):
        if board[i][j] =='R': board[i][j] = 'G'

#print(board)
cnt = 0
v = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if v[i][j] == 0:
            bfs(i,j)
            cnt +=1

print(cnt)