import math

n = int(input())
g = 0
a = []
b = []
for i in range(n):
    a.append(int(input()))
    g = math.gcd(abs(a[i]-a[i-1]),g)
    if i == 1:
        g = math.gcd(abs(a[0]-a[1]),g)
    #print("g:"+str(g))

gf = int(g**1/2)

#print(g,gf)

for i in range(2,gf+1):
    if g % i == 0:
        b.append(i)
    #    b.append(g//i)

b.append(g)

#b = sorted(b)
for i in b:
    print(i,end=' ')