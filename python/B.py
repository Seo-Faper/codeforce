import sys
from math import gcd
N,M = map(int,sys.stdin.readline().split())
w = [] # 분모
v = [] # 분자
d = [] # 1 L 당 설탕량
for i in range(N):
    a,b = map(int,sys.stdin.readline().split())
    w.append(a)
    v.append(b)
    d.append(b/a)

for i in range(N):
    for j in range(i,N):
        if d[i] < d[j]:
            tmp1 = d[i]
            d[i] = d[j]
            d[j] = tmp1

            tmp2 = w[i]
            w[i] = w[j]
            w[j] =  tmp2

            tmp3 = v[i]
            v[i] = v[j]
            v[j] = tmp3

print(w)
print(v)
print(d)
_lcm = w[0]
for n in w[1:]:
    _lcm =int(_lcm*n / gcd(_lcm,n))

i = 0
D = 0
while True:
    need = w[i]
    if M < need: 
        need = M
        # 마지막 처리
       # print(need)
      #  print(need * v[i]*_lcm/w[i])
        D+=int(need * v[i]*_lcm/w[i])
        break

    M -= need

   # print(need)
  #  print(need * v[i]*_lcm/w[i]) 
    D+=int(need * v[i]*_lcm/w[i])
    i+=1

K = gcd(D,_lcm)
print(D/K,end='/')
print(_lcm/K)