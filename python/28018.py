import sys
input = sys.stdin.readline
n = int(input())
SE = []

for _ in range(n):
    s,e = map(int, input().split())
    SE.append([s,e])
for i in range(1,n):
    if SE[i-1][0] <= SE[i][0] < SE[i-1][1]:
        pass
    