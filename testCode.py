import itertools

N,M = map(int, input().split())

print(len(list(itertools.combinations(range(N), M))))