n = int(input())
ans = []
for i in range(1,n//2):
    if n % i == 0:
        if n//i != i:
            ans.append(i)
            ans.append(n//i)
        else:
            ans.append(i)

print(sum(ans)*5-24)