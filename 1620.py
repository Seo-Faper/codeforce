import sys

N,M = map(int, sys.stdin.readline().split())
d = dict()
b = dict()
for i in range(1,N+1):
    k = sys.stdin.readline().replace("\n", "")
    d[i] = k
    b[k] = i


for i in range(M):
    q = sys.stdin.readline().replace("\n", "")
    if q.isdigit():
        print(d[int(q)])
    else:
        print(b[q])

