import math
N = int(input())
M = int(input())
ans =[]
for i in range(N,M+1):
    if int(math.sqrt(i))==math.sqrt(i):
        ans.append(i)
if ans:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)