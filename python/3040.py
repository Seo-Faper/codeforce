
import itertools
L = [int(input()) for _ in range(9)]
for i in itertools.combinations(L, 7):
    if sum(i) == 100:
        for j in i:
            print(j,end='')