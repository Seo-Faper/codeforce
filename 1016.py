'''
어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다. 
제곱수는 정수의 제곱이다. 
min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.
1 ≤ min ≤ 1,000,000,000,000
min ≤ max ≤ min + 1,000,000

1000000000000 1000001000000
'''
import math
a,b= map(int, input().split(" "))
L = []

for i in range(a,b+1):
    L.append(i)

n = int(math.sqrt(L[len(L)-1]))

R = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if R[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        R[j] = False
print(primes)
print(len(primes))
