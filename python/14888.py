import itertools
import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
P = list(map(int, sys.stdin.readline().split()))
operater = []
t = ['+','-','*','/']
for i in range(4):
    for j in range(P[i]):
        operater.append(t[i])

Max = -1e9
Min = 1e9

for i in itertools.permutations(operater,n-1):
    result = A[0]
    for j in range(1,n):
        if i[j-1] == '+':
            result += A[j]
        elif i[j-1] == '-':
            result -= A[j]
        elif i[j-1] == '*':
            result *= A[j]
        else:
            result //= A[j]
    Min = min(Min,result)
    Max = max(Max,result)

print(Max)
print(Min)