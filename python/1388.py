
n,m = map(int, input().split())
graph = [list(input()) for _ in range(n)] 

count = 0
for i in range(n):
    a = ''
    for j in range(m):
        if graph[i][j] == '-':
            if graph[i][j] != a:
                count += 1
        a = graph[i][j]
 

for j in range(m):
    a = ''
    for i in range(n):
        if graph[i][j] == '|':
            if graph[i][j] != a:
                count += 1
        a = graph[i][j]
 
print(count)