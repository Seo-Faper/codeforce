T = int(input())
for _ in range(T):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    flag = True
    for i in range(0,n-1):
        if l[i] % l[i+1] == 0:
            flag = False
            break
        else:
            l[i+1] = l[i] % l[i+1]
    if flag: print("YES")
    else: print("NO")