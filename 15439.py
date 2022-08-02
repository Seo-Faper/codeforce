import itertools
n = int(input())
ans = 0
for i in itertools.permutations(range(n), 2):
    ans +=1
print(ans)