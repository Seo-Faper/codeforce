import sys
N,M = map(int,sys.stdin.readline().split())
D = dict()
for i in range(N):
    a = sys.stdin.readline().replace("\n","").split()
    D[a[0]] = a[1]

#print(D)
for i in range(M):
    s = sys.stdin.readline().replace("\n","")
    print(D[s])
