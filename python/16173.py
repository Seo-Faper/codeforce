

def dfs(x,y):

    if x>=n or x < 0 or y>=n or y < 0 or visited[x][y]:
        return
    if board[x][y] == -1:
        visited[x][y] = True
        return
    visited[x][y] = True
    dx = x + board[x][y]
    dy = y + board[x][y]

    dfs(dx,y)
    dfs(x,dy)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dfs(0,0)
print("HaruHaru" if visited[n-1][n-1]  else "Hing")