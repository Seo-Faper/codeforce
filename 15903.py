#
# 4 2
# 4 2 3 1
# 1 2 3 4
# (1,2) -> 3,3,4,4
# 6, 6, 4, 4 
#
'''
5 3 
5 3 2 1 4

'''
import heapq
heap = []
N,M = map(int,input().split())
L = list(map(int,input().split()))


for i in L:
    heapq.heappush(heap, i)

for i in range(M):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    t = a+b
    heapq.heappush(heap, t)
    heapq.heappush(heap, t)
ans = 0
print(sum(heap))