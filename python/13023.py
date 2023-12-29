import sys
sys.setrecursionlimit(10000)
def dfs(v):
    visited[v] = True
    for e in graph[v]:
        if not visited[e]:
            dfs(e)
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]  
visited = [False]*(n+1)
for _ in range(m):
    x,y = map(int,input().split()) 
    graph[x].append(y) 
    graph[y].append(x)
#print(graph)
count = 0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count+=1
print(count)
