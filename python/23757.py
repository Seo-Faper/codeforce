import heapq
heap = []
N,M = map(int,input().split())
L = list(map(int,input().split()))
R = list(map(int,input().split()))

for i in L:
    heapq.heappush(heap, -1*i)
    
ans = 1
for i in R:
    P = (-1*heapq.heappop(heap))
    if P < i: ans = 0
    else: heapq.heappush(heap, -1*(P-i))
print(ans)