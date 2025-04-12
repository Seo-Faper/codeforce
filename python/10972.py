
n = int(input())
l = list(map(int, input().split()))
def sol(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1:] = reversed(arr[i + 1:])
    return True

if sol(l):
    print(' '.join(map(str,l)))
else:
    print(-1)