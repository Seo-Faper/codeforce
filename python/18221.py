import math
n = int(input())
board = [list(map(int, input().split()))  for _ in range(n)]

posP = [0,0]
posS = [0,0]
for i in range(n):
    for j in range(n):
        if board[i][j] == 5:
            posP = [i,j]
        if board[i][j] == 2:
            posS = [i,j]


startX = min(posP[0], posS[0])
endX = max(posP[0], posS[0])

startY = min(posP[1], posS[1])
endY = max(posP[1], posS[1])

cnt = 0
for i in range(startX, endX+1):
    for j in range(startY, endY+1):
        if board[i][j] == 1:
            cnt+=1

if cnt >=3 and math.sqrt((posP[0] - posS[0])**2 + (posP[1] - posS[1])**2) >= 5:
    print(1)
else:
    print(0)