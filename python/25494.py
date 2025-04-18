T = int(input())
for _ in range(T):
    a,b,c = map(int, input().split())
    count = 0
    for i in range(1, 61):
        for j in range(1, 61):
            for k in range(1, 61):
                if i % j == j % k == k % i == 0 and i <= a and j <= b and k <= c:
                    count +=1
    print(count)