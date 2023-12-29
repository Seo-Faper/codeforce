n = int(input())
board = [list(map(int, input().split( ))) for _ in range(n)]
b = 0
w = 0

def solution(x,y,N):
    global b,w
    color = board[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if color != board[i][j]:
                solution(x, y, N//2)
                solution(x+N//2, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        w+=1
    else: b+=1

solution(0, 0, n)
print(w)
print(b)