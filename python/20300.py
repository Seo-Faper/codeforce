n = int(input())
l = list(map(int, input().split()))
l.sort()
left = l[:n//2]
right = []
last = 999_999_999
if n % 2== 0:
    right = list.copy(l[n//2:])
else:
    right = list.copy(l[n//2:])
    right.pop()
    last = l[n-1]
right.sort(reverse=True)
#print(left, right,last)
ans = last
for i in range(n//2):
    ans = max(ans, left[i]+right[i])

print(ans)