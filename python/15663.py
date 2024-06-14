arr = []
def recur(number):
    if number == M :
        print(*arr)
        return

    last = 0  
    for i in range(N):
        if last == L[i]: continue
        if vis[i] == 1: continue
        arr.append(L[i])
        last = L[i]
        vis[i] = 1
        recur(number + 1)
        vis[i] = 0
        arr.pop()
        
N,M = map(int, input().split())
vis = [0]*N
L = sorted(list(map(int,input().split())))
recur(0)
