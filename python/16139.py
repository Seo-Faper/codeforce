'''
seungjaehwang
4
a 0 5
a 0 6
a 6 10
a 7 10

0
1
2
1
'''
import sys
def f(i):
    return ord(i)-97
S = sys.stdin.readline().replace("\n", "")
q = int(input())
R = list(map(f,S))

for i in range(1,len(R)):
    R[i] += R[i-1]

print(R)