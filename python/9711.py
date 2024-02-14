n = int(input())
dp = [0] * 10001
dp[0] = 1
dp[1] = 1
dp[2] = 1
for i in range(3,10001):
    dp[i] = dp[i-2] + dp[i-1]
for i in range(1,n+1):
    p,q = map(int, input().split())
    print("Case #"+str(i)+": "+str(dp[p]%q))