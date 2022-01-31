import sys
save_list = [[[0 for _ in range(21)] for _ in range (21)] for _ in range (21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if save_list[a][b][c] :
        return save_list[a][b][c]

    if a<b<c :
        save_list[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
    else:
        save_list[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)

    return save_list[a][b][c]
while(True):
    a,b,c = map(int,sys.stdin.readline().split())

    if (a,b,c) == (-1,-1,-1): break
    print("w(%d,%d,%d) = %d"% (a,b,c,w(a,b,c)))