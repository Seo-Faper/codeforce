import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N,M,R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 1
#print(graph)
def dfs(R):
 #   print(f"dfs({R},{cnt}), visited = {visited}")
    global cnt
    visited[R] = cnt
    for nx in sorted(graph[R],reverse=True):
        if not visited[nx]:
            cnt += 1
            visited[nx] = cnt
            dfs(nx)

dfs(R)
for i in range(1, N+1):
    print(visited[i])