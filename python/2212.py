n = int(input())
k = int(input())
array = list(map(int, input().split()))

array.sort()
gap = []
for i in range(1,n):
    gap.append(abs(array[i]-array[i-1]))
gap.sort()
ans = 0

for i in range(0,n-k):
    ans +=gap[i]
print(ans)