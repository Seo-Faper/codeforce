from math import gcd
import sys
input = sys.stdin.readline
print = sys.stdout.write
def prime_factors(n):
    if n <=0: return 0
    i = 2
    factors = {}
    while i * i <= n:
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = 1
    return factors

def find_combinations(a, b,l):
    l_factors = prime_factors(l)
    size = 1
    if l_factors:
        size = max(l_factors.values())+1
    combinations = 0

    ans = []
    for x in range(0, size):
        for y in range(0, size):
            if l % (a**x * b**y) == 0:
              #  print((a**x * b**y), l, gcd((a**x * b**y),l))
                ans.append(((a**x * b**y), l, gcd((a**x * b**y),l)))
                combinations += 1
                # print(k,x,y)
    return len(set(ans))

T = int(input())
for _ in range(T):
    a,b,l = map(int,input().split())
    print(str(find_combinations(a,b,l))+"\n")