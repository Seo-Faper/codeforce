import sys
sys.setrecursionlimit(10**9)
def f(board,x,y):
    global count
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    if board[x][y] == 0:
        return
    count +=1
    board[x][y] = 0
    f(board,x-1,y)
    f(board,x+1,y)
    f(board,x,y-1)
    f(board,x,y+1)
    return count
t = int(input())
ans = []

for i in range(t):
    count = 0
    n,m,k = map(int,input().split())
    board = [[0 for i in range(m)] for i in range(n)]

    for j in range(k):
        x,y = map(int,input().split())
        board[x][y] = 1
    

    l = []
    count = 0
    for a in range(0,n):
        for b in range(0,m):
            if f(board,a,b):
                l.append(f(board,a,b))
    ans.append(len(l))
    

for i in ans:
    print(i)
            
