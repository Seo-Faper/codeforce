def f(n):
    return int(n)*int(n)
L = list(map(f,input().split()))
print(sum(L)%10)