'''
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1

9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
'''
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def solution(operations):
    answer = []
    d = defaultdict(int)
    min_heap = []
    max_heap = []
    for o in range(operations):
        oper, num = input().split()
        num = int(num)
        if oper == 'I':
            d[num] += 1
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        else:
            if num == 1:
                while(max_heap):
                    max_num = -heapq.heappop(max_heap)
                    if d[max_num] != 0:
                        d[max_num] -= 1
                        break
            else:
                while(min_heap):
                    min_num = heapq.heappop(min_heap)
                    if d[min_num] != 0:
                        d[min_num] -= 1
                        break
    
    while(max_heap and d[-max_heap[0]] == 0): heapq.heappop(max_heap)
    while(min_heap and d[min_heap[0]] == 0): heapq.heappop(min_heap)

    if not max_heap: print('EMPTY')
    else: print(-max_heap[0], min_heap[0])

T = int(input())
#print(T)
for _ in range(T):
    k = int(input())
    solution(k)