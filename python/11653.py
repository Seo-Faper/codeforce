
n = int(input())
ans = []
tmp = 2
while(n != 1):
    if n % tmp == 0:
        n //= tmp
        print(tmp)
    else:
        tmp +=1

