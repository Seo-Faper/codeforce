import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(x, y, N, M, board):
    
    if x == N - 1 and y == M - 1:
        return 1  
   
    if dp[x][y] != -1:
        return dp[x][y]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    path_count = 0
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
       
        if 0 <= nx < N and 0 <= ny < M and  board[nx][ny] < board[x][y]:
            path_count += dfs(nx, ny, N, M, board)
    
    dp[x][y] = path_count

    return dp[x][y]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]* M for _ in range(N)]


print(dfs(0, 0, N, M, board))
