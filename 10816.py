import sys
from collections import Counter
n = int(sys.stdin.readline())
L = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
R = list(map(int, sys.stdin.readline().split()))
C = Counter(L)
print(' '.join(f'{C[m]}' if m in C else '0' for m in R))