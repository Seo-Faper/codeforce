import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    groups = {}
    survivor = None
    max_k = 0
    for i, v in enumerate(a):
        if v == -1:
            survivor = i
        else:
            groups.setdefault(v, []).append(i)
            if v > max_k:
                max_k = v
    print(groups, survivor, max_k)
    p = [0] * n
    low, high = 1, n

    for k in range(1, max_k + 1):
        if k in groups:
            if k % 2 == 1:
                for idx in groups[k]:
                    p[idx] = high
                    high -= 1
            else:
                for idx in groups[k]:
                    p[idx] = low
                    low += 1

    if survivor is not None:
        p[survivor] = low

    print(*p)
