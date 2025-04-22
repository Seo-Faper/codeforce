H,W = map(int, input().split())
board = [[0]*W for _ in range(H)]
l = list(map(int, input().split()))
for i in range(len(l)):
    for j in range(l[i]):
        board[j][i] = 1

ans = 0

for i in range(H):
    wall_cnt = 0
    water_tmp = 0
    for j in range(W):
        if board[i][j] == 1:
            if wall_cnt > 0 and water_tmp > 0:
                ans += water_tmp
            water_tmp = 0
            wall_cnt += 1
        elif board[i][j] == 0 and wall_cnt > 0:
            water_tmp += 1
print(ans)