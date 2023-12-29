T = int(input())
for i in range(T):
    N = int(input())
    L = [int(input()) for _ in range(N)]
    m = 1
    t = []
    for j in L:
        t.append(j%m)
        m+=1
        