from collections import deque
N = int(input())
deq = deque()
L = list(map(int,input().split()))
for i in range(1,N+1):
    d = [i,L[i-1]]
    deq.append(d)

while len(deq) != 0:
    p = deq.popleft()
    print(p[0],end=' ')
    if p[1] < 0:
        deq.rotate(-p[1])
    else:
        deq.rotate(-p[1]+1)
   # break