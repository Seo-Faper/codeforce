import sys
N = int(sys.stdin.readline())
L = []
for i in range(N):
    L.append(int(sys.stdin.readline()))

L = sorted(L)
ans = 0
for i in range(len(L)):
    ans = max(L[i]*(N-i),ans)

print(ans)