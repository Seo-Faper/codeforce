
N = int(input())
l = list(map(int,input().split()))
l.sort()
ans = 0
for i in range(N):
    target = l[i]
    left = 0
    right = N-1
    while left < right:
        _sum = l[left] + l[right]
        #print(_sum)
        if target == _sum:
            if left != i and right != i:
                ans += 1
                break
            elif left == i:
                left+=1
            else:
                right-=1
        elif target < _sum:
            right -= 1
        else:
            left += 1
print(ans)
