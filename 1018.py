def S(x,y):
    A = 0
    B = 0
    for i in range(8):
        for j in range(8):
            if P1[i][j] != board[x+i][y+j]:
                A+=1
            if P2[i][j] != board[x+i][y+j]:
                B+=1
    return min(A,B)


P1 = [
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
    ]
P2 = [
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
    ]
N,M = map(int,input().split())
board = [[x for x in input()]for y in range(N)]
ans = []

for i in range(N-7):
    for j in range(M-7):
        ans.append(S(i,j))        

print(min(ans))