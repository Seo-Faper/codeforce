import itertools
N,M = map(int,input().split())
L = sorted(list(map(int,input().split())))
v = [False]*N
temp = []
def f(index):
    global v,temp
    if len(temp)==M:
        print(*temp)
    
    for i in range(len(L)):
        if v[i]:
            continue
        v[i] = True
        temp.append(L[i]) 
        f(index+1)
        v[i] = False
        temp.pop()

f(0)