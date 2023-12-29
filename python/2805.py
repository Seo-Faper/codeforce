
K,N = map(int, input().split())
L = list(map(int, input().split()))
# print(L)

ans = 0
start = 0
end = 2000000000
while start <= end:
    mid =  ( start + end ) // 2
    tmp = 0
    for i in L:
       if i > mid:
           tmp += (i - mid)
    if tmp >= N: 
        ans = mid
        start = mid + 1 
    else:
        end = mid -1

print(ans)
