n = int(input())
l = list(map(int, input().split()))
# 1 1 1 1 0 1 2 0

ans = 0
tmp = 0
for i in l:
    if i == tmp:
       tmp += 1
       ans +=1 
    tmp %= 3
print(ans)