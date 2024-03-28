N = int(input())
K = int(input())
l = []
for i in range(1,N+1):
    for j in range(1,N+1):
        l.append(i*j)
print(l)