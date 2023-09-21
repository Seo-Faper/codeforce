from itertools import permutations
N = int(input())
l = [ x for x in range(N)]
permute = permutations(l,N)
for i in permute:
    for j in i:
        print(j+1,end=' ')
    print()