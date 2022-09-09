ans = []
N = int(input())
L = [list(input()) for _ in range(N)]
def f(i,j,n):
    sol = L[i][j]
    status = False
    for x in range(i,i+n):
        if set(L[x][j:j+n]) != set(sol):
            status = True
    if not status:
        ans.append(sol)
        return

    n //=2 
    ans.append("(")
    f(i,j,n)
    f(i,j+n,n)
    f(i+n,j,n)
    f(i+n,j+n,n)
    ans.append(")")

f(0,0,N)
for i in ans:
    print(i,end='')