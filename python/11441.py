n = int(input())
arr = list(map(int, input().split()))
ori = list.copy(arr)
for i in range(1,n):
    arr[i] += arr[i-1]
m = int(input())
print(arr)
for _ in range(m):
    i,j = map(int, input().split())
    if i == 1:
        print(arr[j-1])
    elif i == j:
        print(ori[j-1])
    else: print(arr[j-1] - arr[i-2])