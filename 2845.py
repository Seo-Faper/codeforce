L,P = map(int,input().split())
A = list(map(int,input().split()))
t = L*P
for i in A:
    print(i-t,end=' ')