'''
1924 , 2의 경우
제일 처음 1 입력
1에 대하여 9가 더 크니까 교체
교체했으니까 다음 2 입력
92 됐음
2에 대하여 4가 더 크니까 교체
94 종료

4 2
1924

1 924
9 24

7 3
1231234 의 경우

1 231234

2 31234 // 1개 지워짐
3 1234 // 2개 지워짐
31 234 // 3개 지워짐 
32 34 결론 

10 4
4177252841






'''

import sys
N,K = map(int,sys.stdin.readline().split())
L = list(map(int,sys.stdin.readline().strip()))
A = []
D = K

for i in range(N):
    while D > 0 and A:
        if A[len(A)-1] < L[i]:
            A.pop()
            D-=1
        else:
            break
    A.append(L[i])
    
for i in range(N-K):
    print(A[i],end="")