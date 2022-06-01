def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)
n = input()
L = list(map(int,input().split(" ")))
for i in range(1,len(L)):
    t = gcd(L[0],L[i])
    print(str(L[0]//t)+"/"+str(L[i]//t))

