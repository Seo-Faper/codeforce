n = int(input())
arr = list(map(int, input().split()))
lis = [arr[0]]
for i in range(1,n):
    if lis[-1] <= arr[i]:
        lis.append(arr[i])
    else:
        start, end = 0, len(lis)-1
        while start <= end:
            mid = (start + end)//2
            if arr[i] <= lis[mid]:
                end = mid - 1
            else:
                start = mid + 1
        lis[start] = arr[i]

print(len(lis))