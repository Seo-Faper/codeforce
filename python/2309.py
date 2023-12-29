import itertools
L = []
for i in range(9):
    L.append(int(input()))

L = sorted(L)
print(L)
for i in itertools.combinations(L, 7):
    if sum(i)==100:
        
        for j in i:
            print(j)
        break