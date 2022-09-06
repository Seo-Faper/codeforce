import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
b = list(map(int, input().split()))
ans = abs(100 - target)

for i in range(1000001):
    i = str(i)
    for j in range(len(i)):
        if int(i[j]) in b: break
        elif j == len(i)-1:
            ans = min(ans,abs(int(i) - target)+len(i))

print(ans)