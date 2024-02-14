n = int(input())
p = [350.34,230.90,190.55,125.30,180.90]
for i in range(n):
    l = list(map(int, input().split()))
    ans = 0.0
    for i in range(len(l)):
        ans += p[i]*l[i]
    print("$"+format(ans,".2f"))