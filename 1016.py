'''
어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다. 
제곱수는 정수의 제곱이다. 
min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.

a <= X <= b

1,2,3,4,5,6,7,8,9,10 에서

1보다 큰 제곱수로 나누어 지지 않는다? 
16 선에서 해결 가능?

1 x
2 x
3 x 
4 o (4%4 == 0)
5 x 
6 x
7 x
8 o (8%4 == 0)
9 o (9%9 == 0)
10 x

총 3개 를 제외한 7개가 제곱 ㄴㄴ 수 

20,30 이라고 하면 그 사이의 소수는 무조건 제곱 ㄴㄴ 수 
약수 중에 제곱수가 없으면 그것도 제곱 ㄴㄴ 수

4,9,16,25,36,49,64,81,100,121,141,169 ... 을 약수로 가지지 않아야 하는데

1 ≤ min ≤ 1,000,000,000,000
min ≤ max ≤ min + 1,000,000

최대 1 <= X <=1000001000000 사이의 제곱 ㄴㄴ 수를 찾는다 치면

근데 사실 저렇게는 안되고 범위의 차이는 1000000 밖에 안된다는 소리

1. max에 루트를 씌워서 최소 제곱 수를 찾는다
max = 10 이면 3이 최대 제곱 부모니까 [4,9] 까지만 가진다.
math.sqrt(max)//1 하면 3.xxx //1 해서 3이 나오는 원리? < ㅇㅈ

ex) 1,1000

루트 1000 = 31.xxxx 이므로 31 보다 큰 제곱 수는 36 

[4,9,16,25,36,49,64,81,100,121,] 


'''
import math
a,b= map(int, input().split(" "))
L = []
K = []
flag = True
start = 0
for i in range(a,b+1):
    L.append(i)
    if i != 1 and flag and round(math.sqrt(i)) == math.sqrt(i):
        start = int(math.sqrt(i))
        flag = False

R = [True]*(b-a+1)

ans = 0
for i in range(start,int(math.sqrt(b)//1)+1):
    k = i*i
    if i > 3 and R[b+1-k]:
        for j in range(k,b-a+2,k):
            R[j] = False
            

for i in R:
    if i : ans+=1
print(ans)