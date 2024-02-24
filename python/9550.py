T = int(input())

for i in range(T):
    N,K = map(int, input().split())
    l = list(map(int,input().split()))
    ans = 0
    for j in l:
        ans += j//K
    print(ans)