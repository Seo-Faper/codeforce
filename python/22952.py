n = int(input())
ans = [n]
for i in range(1,n//2):
    ans.append(i)
    ans.append(n-i)
ans.append(n//2)
if n==1:
    print(1)
    exit(0)
if n %  2 == 1 : ans.append(n//2+1)

print(*ans)