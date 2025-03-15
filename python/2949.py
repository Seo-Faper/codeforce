def rotate90(r,c,board):
    new_board = []
    for i in range(c):
        tmp = []
        for j in reversed(range(r)):
            tmp.append(board[j][i])
        new_board.append(tmp)
    return len(new_board), len(new_board[0]),new_board

def rotate45(r,c,board):
    new_board = []
    for _ in range(r+c):
        new_board.append(list(' '*(r+c)))

    for i in range(r):
        line = board[i]
        #print(line)
        for x in range(c):
            new_board[i+x][r+x-i] = line[x]

    for i in range(len(new_board[1:])):
        s = ''.join(new_board[i])[1:].rstrip()
        print(s)
    return new_board   

r,c = map(int, input().split(" "))
board = []
for i in range(r):
     board.append(list(input()))
#print(board)
k = int(input()) // 45
for _ in range(k//2):
    r,c, board = rotate90(r,c,board)
#print(board)
if k % 2 == 0:
    for i in range(len(board)):
        print(''.join(board[i]))
for _ in range(k % 2):
    rotate45(r,c,board)