
l = []

def DFS(d,x,y):
    if d == y:
        print(' '.join(map(str,l)))
        return
    else:
        for i in range(x):
            l.append(i+1)
            DFS(d+1,x,y)
            l.pop()
         

n, m = map(int, input().split())
DFS(0,n,m)