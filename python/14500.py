def type0(x,y): # 가로 4블럭
    sum = 0
    for i in range(x,x+1):
        for j in range(y,y+4):
            sum +=board[i][j]
    return sum
def type1(x,y): # 세로 4블럭
    sum = 0
    for i in range(x,x+4):
        for j in range(y,y+1):
           sum += board[i][j] 
    return sum

def type2(x,y): # 2x2 블럭 
    sum = 0
    for i in range(x,x+2):
        for j in range(y,y+2):
            sum += board[i][j]
    return sum
def type3(x,y): #3x2 블럭
    sum = 0
    for i in range(x,x+2):
        for j in range(y,y+3):
            sum += board[i][j]
    return max(sum - board[x][y] - board[x+1][y+2], sum - board[x+1][y] - board[x][y+2], 
               sum - board[x][y+1]- board[x][y+2], sum - board[x+1][y+1] - board[x+1][y+2],
               sum - board[x][y] -  board[x][y+2], sum - board[x+1][y] - board[x+1][y+2],
               sum - board[x][y] - board[x][y+1], sum- board[x+1][y] - board[x+1][y+1])

def type4(x,y): # 2x3 블럭
    sum = 0
    for i in range(x,x+3):
        for j in range(y,y+2):
            sum += board[i][j]
    return max(sum - board[x][y] - board[x+2][y+1], sum - board[x][y+1] - board[x+2][y],
               sum - board[x][y] - board[x+1][y], sum - board[x][y+1]- board[x+1][y+1],
               sum - board[x+1][y+1] - board[x+2][y+1] , sum - board[x+1][y] - board[x+2][y],
               sum - board[x][y] - board[x+2][y], sum - board[x][y+1] - board[x+2][y+1])

N,M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split(" "))))
ans = 0
for i in range(N):
    for j in range(M):
        try:
            ans = max(type0(i,j),ans)
        except:
            pass
        try:
            ans = max(type1(i,j),ans)
        except:
            pass
        try:
            ans = max(type2(i,j),ans)
        except:
            pass
        try:
            ans = max(type3(i,j),ans)
        except:
            pass
        try:
            ans = max(type4(i,j),ans)
        except:
            pass


print(ans)