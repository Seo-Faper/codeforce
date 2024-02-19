import sys

A,B = map(int, input().split())

if A==B: print(0)
else:
    print(abs(B-A)-1)
    for i in range(min(A,B)+1, max(A,B)):
        sys.stdout.write(str(i)+" ")
    print()