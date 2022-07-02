import sys

def f(x,a,b):
    if a == 0 and b ==0 :
        return 1
    else:
        return a*x+b

N = int(sys.stdin.readline())
x = 0
f = 1
a = 0
b = 0
F = "1"

for i in range(N):


    Q = list(map(int,sys.stdin.readline().split()))
    if len(Q)==3:
        a = Q[1]
        b = Q[2]
            
    else:
        x = Q[1]
