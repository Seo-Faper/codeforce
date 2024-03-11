def f(n):
    p = 0
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            if i == n//i:
                p+= i
            else:
                p += i +  n // i 
    return p
n = int(input())

ans = 0
for i in range(1,n+1):
    ans += f(i)
print(ans)