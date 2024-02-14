n = int(input())
m = int(input())
l = list(map(int, input().split()))

ans = 0
for i in l:
    if m - i in l:
        ans +=1
print(ans//2)