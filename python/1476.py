def f(n):
    return int(n)+1
ESM= list(map(int,input().split()))

# 1<=E<=15
# 1<=S<=28
# 1<=M<19

L = [1,1,1]
ans = 1
while(ESM != L):
    ans+=1
    L = list(map(f,L))
    if L[0] > 15:
        L[0] = 1
    if L[1] > 28:
        L[1] = 1
    if L[2] > 19:
        L[2] = 1


print(ans)