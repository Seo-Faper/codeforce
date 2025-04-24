from itertools import combinations
pos = {}
pool = set()
xs = set()
for _ in range(int(input())):
    x,y = map(int, input().split())
    xs.add(x)
    pool.add((x,y))
    if x in pos:
        pos[x].append(y)
    else:
        pos[x] = [y]

ans = 0

for x1,x2 in combinations(xs, 2):
    y1 = pos[x1]
    y2 = pos[x2]
    for i in y1:
        for j in y2:
            if i!=j:
                pos1 = (x1, i)
                pos2 = (x2, j)
                pos3 = (x1, j)
                pos4 = (x2, i)
                if pos1 in pool and pos2 in pool and pos3 in pool and pos4 in pool:
                    ans +=1

print(ans//2)