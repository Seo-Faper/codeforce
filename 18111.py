from math import inf
from sys import stdin
N, M, B = map(int, stdin.readline().split())
world = [list(map(int, stdin.readline().split())) for _ in range(N)]
ans = inf
t = 0

for i in range(257):
    a = 0
    b = 0
    for j in range(N):
        for k in range(M):
            if world[j][k] < i:
                a +=(i - world[j][k])       
            else:
                b +=(world[j][k] - i)
        inv = b + B
        
    if inv < a:
        continue
    time = 2*b+a
    if time <= ans:
        ans = time
        t = i

print(ans,t)