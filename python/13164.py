n,k = map(int, input().split())
ans = 0
array = list(map(int, input().split()))
key_gap = []
for i in range(1,len(array)):
    key_gap.append(array[i] - array[i-1])
key_gap.sort()
for i in range(0,n-k):
    ans += key_gap[i]
print(ans)