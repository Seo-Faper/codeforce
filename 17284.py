M = [0,500,800,1000]
L = list(map(int,input().split()))

ans = 5000
for i in L:
    ans -=M[i]

print(ans)