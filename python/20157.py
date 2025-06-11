import math

N = int(input())
arr = {}
ans = 0

for _ in range(N):
    x, y = map(int, input().split())

    g = math.gcd(x, y)
    
    rx = x // g
    ry = y // g
        
    pos = (rx, ry)
    
    if pos in arr:
        arr[pos] += 1
    else:
        arr[pos] = 1

if arr:
    ans = max(arr.values())
else: # 
    ans = 0

print(ans)