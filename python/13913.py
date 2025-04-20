from collections import deque
n,k = map(int, input().split())

visited = [0] * (100_001)
visited[n] = 1
q = deque()
q.append((n,0))
way = [-1]*(100_001)
while q:
    x, cnt = q.popleft()
    if x == k:
        print(cnt)
        break
    
    for nx in (x-1, x+1, x*2):
        if 0 <= nx <= 100000 and not visited[nx]:
            visited[nx] = 1
            q.append((nx, cnt+1))   
            way[nx] = x

path = []
cur = k
while cur != -1:
    path.append(cur)
    if cur == n:
        break
    cur = way[cur]
path.reverse()

print(*path)