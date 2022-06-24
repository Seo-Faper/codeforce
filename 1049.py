n,m = map(int,input().split())
A = []
B = []
for i in range(m):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)


A1 = min(A)
B1 = min(B)

needSix = n//6
if n % 6 != 0: needSix +=1

ans = 0
while True:
    sel = 0 
    t = 0
    if n < 6:
        sel = min(B1*n,A1)
        t = n
    else:
        sel = min(A1,B1*6)
        t = 6

    n -= t
    ans +=sel
    if n <= 0 : break

print(ans)