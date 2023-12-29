import sys

n = int(sys.stdin.readline().replace("\n", ""))
l = list(map(int, sys.stdin.readline().replace("\n", "").split()))

r = list(sorted(set(l)))

d = {value: index for index , value in enumerate(r)}


for i in l:
    print(d[i],end=' ')