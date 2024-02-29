import math
T = int(input())
for _ in range(T):
    n = int(input())
    if n == 1:
        print(1)
    else:
        print(2**int(math.log(n,2)))