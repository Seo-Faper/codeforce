n = int(input())
pos = [list(map(int, input().split())) for _ in range(n)]
ans = [1e9] * n
for xs in pos:
    for ys in pos:
        distance = []
        for x,y in pos:
            distance.append(abs(xs[0] - x) + abs(ys[1] - y))
        distance.sort()
        tmp = 0
        for i in range(n):
            tmp += distance[i]
            ans[i] = min(ans[i],tmp)
print(*ans)