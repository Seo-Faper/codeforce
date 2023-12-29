A,B = map(int,input().split())
L = []
for i in range(1,B+1):
    for j in range(1,i+1):
        L.append(i)

print(sum(L[A-1:B]))