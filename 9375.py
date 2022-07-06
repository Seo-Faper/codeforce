import itertools
T = int(input())
for i in range(T):
    n = int(input())
    L = [input().split()[1] for _ in range(n)]
    #print(L)
    R = list(set(L))
    #print(R)
    ans = 1
    N = []
    for i in R:
        N.append(L.count(i)+1)
    
   # print(N)
    for i in N:
        ans *=i
    print(ans-1)
    