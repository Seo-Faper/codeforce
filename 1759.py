import itertools
#  itertools.combinations(k[1:],6)

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        print(cycles)
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:

                indices[i:] = indices[i+1:] + indices[i:i+1]

                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

L,C = map(int, input().split())
k = input().split()
for i in permutations(k, L):
    i2 = sorted(i)

    if i2 == list(i):
        for j in i: 
            print(j,end='')
        print()

# 14 15
# a b c d e f g h i j k l m n o 