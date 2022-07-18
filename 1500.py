N,K = map(int,input().split())

a = N // K
b = N % K


L = [a]*K

for i in range(b):
    L[i] +=1

ans = 1
for i in L:
    ans *=i

print(ans)