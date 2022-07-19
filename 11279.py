import heapq
N = int(input())
heap = []
ans = []
for i in range(N):
    t = int(input())
    if len(heap) == 0 and t == 0:
        ans.append(0)
    elif t == 0 :
        ans.append(-1*heapq.heappop(heap))
    else:
        heapq.heappush(heap, -1*t)

for i in ans:
    print(i)