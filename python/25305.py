N,K = map(int,input().split())
L = list(map(int,input().split()))
L = sorted(L,reverse=True)
print(L[K-1])