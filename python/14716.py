import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
M,N = map(int, input().split())
board = [[0]*N for _ in range(M)]
for i in range(M):
    board[i] = list(map(int, input().split()))
visited = [[0]*N for _ in range(M)]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [1, 1, 1, 0, -1, -1, -1, 0]
def dfs(x, y):
    visited[x][y] = 1

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == 1:
            dfs(nx, ny)
ans = 0
for i in range(M):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            ans +=1

print(ans)