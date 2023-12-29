import itertools
N,K = map(int,input().split())

for i in itertools.product(range(N),range(N),range(N),range(N)):
    print(i,end = ' ')