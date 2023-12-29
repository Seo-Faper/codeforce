import sys
import heapq
n = int(sys.stdin.readline())

heap = []
ans = []
for _ in range(n):
    i = int(sys.stdin.readline())
    if i == 0 and heap:
        ans.append(heapq.heappop(heap))
    elif i == 0 and len(heap)==0:
        ans.append(0)
    else:
        heapq.heappush(heap, [abs(i),i])

for i in ans:
    if i !=0:
        print(i[1])
    else:
        print(0)