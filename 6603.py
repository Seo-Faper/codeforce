import itertools
while(True):
    k = list(map(int,input().split()))
    if k[0] == 0: break
    for i in itertools.combinations(k[1:],6):
       for k in i :print(k,end=' ')
       print()
    print()