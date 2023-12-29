N = int(input())
for i in range(N):
    _ = input()
    l = [int(x) for x in input().split(" ")]
    a = 0
    b = 0
    for i in l:
        if i % 2== 0: a+=i
        else: b+=i
    if (a+b)%2 ==0:
        print("Yes")
    else: print("No")
