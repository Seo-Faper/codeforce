'''
3
3 4 5
2 2
'''

import sys
N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
T1, T2 = map(int,sys.stdin.readline().split())
ans = N
def f(i):

    if i-T1 < 0: 
        return 0
    else:

        return i-T1
def w(i):
    if i == 0 : return 0
    if i-T2 < 0 : return 1 
    if i % T2 == 0:
        return i//T2
    else:
        return i//T2+1

L = list(map(f,L))

R = list(map(w,L))

print(sum(R)+ans)

