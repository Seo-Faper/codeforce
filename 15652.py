l = []
def DFS(d,n,m):
    if len(l) > 1 and l[len(l)-2] > l[len(l)-1]:
        return

    # 지금 해야 하는 거
    if d == m:
        print(' '.join(map(str, l)))
        return
    else:

        for i in range(n):  
            l.append(i+1)
            DFS(d+1,n,m)
            l.pop()
    # 나중에 해야 하는 거

n,m = map(int,input().split())
DFS(0,n,m)
