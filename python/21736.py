import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m = map(int, input().split())
board = [input() for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans = 0

def dfs(x, y):
    global ans
    if visited[x][y] == 1:
        return
    visited[x][y] = 1
    if board[x][y] == 'X':
        return
    if board[x][y] == 'P':
        ans += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and board[nx][ny] != 'X':
            dfs(nx, ny)

for i in range(n):
    for j in range(m):
        if board[i][j] == 'I' and visited[i][j] == 0:
            dfs(i, j)  
print(ans if ans > 0 else "TT")