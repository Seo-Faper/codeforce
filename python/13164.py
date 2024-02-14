n, k = map(int, input().split())
ans = 0
array = list(map(int, input().split()))

def keying():
    global ans
    global array
    key_gap = []
    for i in range(1, len(array)):
        key_gap.append((array[i] - array[i-1], i))
    key_gap.sort(reverse=True)
    if len(key_gap) == 0:
        return
    middle_index = key_gap[0][1]
    left = array[0:middle_index]
    right = array[middle_index::]
    if len(left) == 0 or len(right) == 0:
        return
    left_gap = left[len(left)-1] - left[0]
    right_gap = right[len(right)-1] - right[0]
    if left_gap > right_gap:
        ans += right_gap
        array = left
    else:
        ans += left_gap
        array = right

if n > k:
    for i in range(1, k):
        keying()
        if len(array) == 0:
            break
    if len(array) > 0:
        print(array[len(array)-1] - array[0] + ans)
    else:
        print(ans)
else:
    print(0)
