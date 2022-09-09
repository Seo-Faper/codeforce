import sys

n,k = map(int,sys.stdin.readline().split())
dp = []                           
for i in range(n):      
  x = int(sys.stdin.readline())
  if(x <= k):
    dp.append(x)                    

if len(dp):       
  s = [0 for i in range(k)] 
  for i in range(len(dp)):     
    s[dp[i]-1] += 1           
    for j in range(dp[i],k):   
      s[j] += s[j-dp[i]]       
  print(s[k-1])
else:
    print(0)