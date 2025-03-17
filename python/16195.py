
T = int(input())
dp = [[0]*1005 for _ in range(1005)]
MOD = 1_000_000_009
dp[1][1] = dp[2][1] = dp[3][1] = 1
dp[2][2] = 1
dp[3][2] = 2
dp[3][3] = 1
for i in range(4,1000+1):
    for j in range(2,1000+1):
        dp[i][j] = (dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1]) % MOD

for _ in range(T):
    n,m = map(int, input().split())
    found = 0
    for i in range(1,m+1):
        found = (found + dp[n][i])%MOD
    print(found)