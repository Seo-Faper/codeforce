N, M = map(int,input().split())
board = [list(input()) for _ in range(N)]
a = 0 
b = 0
for v in board:
  #  print(v)
    if 'X' not in v:
        a+=1

for i in range(M):
    flag = False
    for j in range(N):
        if board[j][i] =='X':
            flag = True
    if not flag:
        b+=1

print(max(a,b))

