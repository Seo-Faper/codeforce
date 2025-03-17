n,s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 100_000_000

total = arr[0]
end = 0
start = 0

while start <= end and end < n:
    if total < s:
        end+=1
        if end < n:
            total += arr[end]
        else:
            break
    else:
        ans = min(ans, end - start+1)
        total -= arr[start]
        start+=1
if ans == 100_000_000: ans = 0
print(ans)