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
ans = b-a+1
A = [False] * (b-a+1)
i = 2
while i*i <= b:

  sn = i*i
  remain = 0 
  if a%sn!=0: remain = 1
  j = a//sn + remain

  while sn*j <=b:
    if not A[sn*j-a]:
      A[sn*j-a] = True
      ans -=1
    j+=1
  i+=1

print(ans)
