
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    a.sort()
    print(abs(a[0] - a[n-1]) + abs(a[n-1] - a[1]) + abs(a[1] - a[n-2]) + abs(a[n-2] - a[0]))