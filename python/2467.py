n = int(input())
l  = list(map(int, input().split()))

left = 0
right = n - 1
init_min = float('inf')

left_val = 0
right_val = 0

while left < right:
    curr = l[left] + l[right]
    if abs(curr) < init_min:
        init_min = abs(curr)
        left_val = l[left]
        right_val = l[right]
    if curr == 0:
        break
    elif curr < 0:
        left += 1
    else:
        right -= 1

print(left_val, right_val)