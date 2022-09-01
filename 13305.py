'''

[ 2,  3, 1]
[5, 2, 1, 4]

i+1 번째 항이 i 보다 작을 때 까지 갱신하지 않는다.

2에서 4로 넘어갔을 때 2<4 이므로 바꾸지 않는다.

5

'''
import math
N = int(input())
R = [0] + list(map(int,input().split()))
R.append(0)
L = list(map(int,input().split()))

now = math.inf
ans = 0
for i in range(N):
    if L[i] < now : now = L[i]
    ans += now * R[i+1]

print(ans)