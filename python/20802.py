n = int(input())
T = list(map(int, input().split()))
P = list(map(int, input().split()))

ans = 0
for i in T:
    ans += i//P[0]
    if i%P[0] != 0:
        ans +=1
print(ans)
print(n//P[1],n%P[1])