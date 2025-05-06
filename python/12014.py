

for num in range(int(input())):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    l = [arr[0]]
    for i in range(1,n):
        if l[-1] < arr[i]:
            l.append(arr[i])
        else:
            start,end = 0, len(l)-1
            while start <= end:
                mid = (start+end)//2
                if l[mid] >= arr[i]:
                    end = mid - 1
                else:
                    start = mid+ 1
            l[start] = arr[i]
    print("Case #"+str(num+1))
    if len(l) >= k:
        print(1)
    else:
        print(0)