N = int(input())
M = int(input())

count = 2
ans = 0
while True:

    N = N * M // 100
    if N <= 5: break

    ans +=count * N
    count *=2
print(ans)