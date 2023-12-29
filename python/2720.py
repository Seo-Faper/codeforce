'''
3
124
25
194

4 2 0 4
1 0 0 0
7 1 1 4

'''
N = int(input())
L = [int(input()) for _ in range(N)]

cents = [25,10,5,1]
for z in L:
    k = z
    ans = [0,0,0,0]
    for i in range(len(cents)):
        ans[i] += k // cents[i]
        k = k % cents[i]
    print(*ans)
    