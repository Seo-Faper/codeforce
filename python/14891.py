def Rotate(L,r):
    if r == 1:
        tmp = L.pop()
        L.insert(0,tmp)
    else:
        tmp = L.pop(0)
        L.append(tmp)
    return L

Ls = [input() for _ in range(4)]

n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    sel = Ls[a-1]    
    Ln = -1 # -1 : 지정되지 않은 상태
    Rn = -1
    if a == 1:
        Rn = Ls[a+1][0]
    elif a == 4:
        Ln = Ls[a-2][4]
    else:
        Ln = Ls[a-2][4]
        Rn = Ls[a+1][0]
        if sel[4] != Rn:
            Ls[a-1] = Rotate(Ls[a-1], b)
            Ls[a+1] = Rotate(Ls[a+1], b)
        
        if sel[0] != Ln:
            Ls[a-1] = Rotate(Ls[a-1], b)


