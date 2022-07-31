import sys

K,N = map(int, input().split())
L = [int(input()) for _ in range(K)]
# print(L)

ans = 0
start = 0
end = sum(L) // N + 1
while start <= end:
    mid =  ( start + end ) // 2
    tmp = 0
    for i in L:
        tmp += i // mid
    if tmp >= N: 
        ans = mid
        start = mid + 1 
    else:
        end = mid -1

print(ans)
