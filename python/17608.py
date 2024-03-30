import sys

input = sys.stdin.readline

l = [int(input()) for _ in range(int(input()))]

l = l[::-1]

_max = l[0]
ans = 1
for i in l:
   # print(_max)
    if _max < i:
        _max = i
        ans+=1
        
print(ans)