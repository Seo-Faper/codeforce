import sys
input = sys.stdin.readline
N,K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
dp = [0]+[10001] * K
#print(coins)
for i in coins:
    for j in range(i,K+1):
        dp[j] = min(dp[j], dp[j - i]+1)
       # print(dp[j - i]+1)
        
if dp[K] == 10001: print(-1)
else:
    print(dp[K])

'''

    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
1   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
5   1 2 3 4 1 2 3 4 5 2  3  4  5  6  3  
12  1 2 3 4 1 2 3 4 5 2  3  1  2  3  4 


dp[i] = min(dp[i] , dp[i-coin] + 1)
dp[15] = min(dp[15], dp[15-12]+1)
dp[15] = min(dp[15], dp[3]+1) 
dp[15] = min(3, 4)
dp[15] = 3 
'''