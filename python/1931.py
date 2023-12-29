import sys
n = int(input())
L = []
for i in range(n):
    L.append(list(map(int,sys.stdin.readline().split())))

L.sort(key = lambda x:(x[1],x[0]))

#print(L)
e = 0
count = 0
for i in L:
    if e <= i[0]:
        e= i[1]
        count+=1
print(count)