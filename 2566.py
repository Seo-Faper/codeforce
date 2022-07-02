board = [list(map(int,input().split())) for i in range(9)]
ans = []
for i in range(9):
    ans.append(max(board[i]))

x = ans.index(max(ans))
y = board[x].index(max(board[x]))
print(max(ans))
print(x+1,y+1)
