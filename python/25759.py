N = int(input())
arr = list(map(int,input().split()))
num_max = [-1] * 110
dp =  [0]*N
for i in range(N):
    for j in range(1,101):
        if num_max[j] == -1: continue
        dp[i] = max(dp[i], num_max[j]+(arr[i]-j)**2)
    num_max[arr[i]] = max(num_max[arr[i]], dp[i])
print(dp[N-1])