n = int(input())
l =  list(map(int, input().split()))
ans = 0
target = list(map(int, input().split()))
def quick_sort(l, target=None):
    global ans
    print(l, target)
    if len(l) <= 1:
        return l
    if target == l:
        ans = 1
        return
    pivot = l[len(l) // 2]
    left = [x for x in l if x < pivot]
    middle = [x for x in l if x == pivot]
    right = [x for x in l if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

quick_sort(l, target)
print(ans)