
N,M = map(int, input().split())
graph = [[int(x) for x in input()] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0: graph[i][j] = 1
        else: graph[i][j] = 0
prefix = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + graph[i-1][j-1]

_max = 0
for i in range(1,N+1):
    for j in range(i,M+1):
        cnt = 0
        for k in range(1,N+1):
            tmp = prefix[k][j] - prefix[k][i - 1] - prefix[k - 1][j] + prefix[k - 1][i - 1]
            if tmp == j - i + 1:
                cnt+=tmp
            else:
                _max = max(_max,cnt)
                cnt = 0
print(_max)