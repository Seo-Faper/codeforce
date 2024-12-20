N, M = map(int, input().split())
l = list(map(int, input().split()))

end = 0
start = 0
ans = 0

while start <= end and end <=N :

    ls = l[start:end]
    _sum = sum(ls)
    if _sum > M:
        start +=1
    elif _sum < M:
        end +=1
    else:
        ans += 1
        end += 1
print(ans)