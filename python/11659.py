import sys
N,M = map(int,sys.stdin.readline().split())
L = list(map(int,sys.stdin.readline().split()))
for i in range(1,N):
    L[i] += L[i-1]
#print(L)  
for i in range(M):
    x,y = map(int,sys.stdin.readline().split())
    if x > 1:
        print(L[y-1]-L[x-2])
    else: 
        print(L[y-1])