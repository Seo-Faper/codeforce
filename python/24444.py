from collections import deque
import sys
input = sys.stdin.readline
N,M,R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)



cnt = 1
def BFS(R):
    global cnt
    q = deque()
    q.append(R)
    visited[R] = 1
    while q:
        x = q.popleft()

        for nx in sorted(graph[x]):
            if not visited[nx]:
                cnt += 1
                visited[nx] = cnt

                q.append(nx)
             
BFS(R)
for i in range(1, N+1):
    print(visited[i])

