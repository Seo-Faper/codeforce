T= int(input())
for i in range(T):
    _ = input()
    l = list(map(int,input().split()))
    ans = sum(list(map(abs,l)))
    print(ans)