'''
입력:
7
1 2 3 3 4 4 5
정답:
1 3 2 4 3 5 4

입력:
8
1 2 3 3 4 5 6 6
정답:
1 3 2 4 3 6 6 5

입력:
5
1 2 3 4 5
정답:
1 3 2 5 4 

입력:
12
1 1 1 2 2 2 3 3 3 4 4 4
정답:
1 1 1 3 2 2 2 4 4 4 3 3


입력:
8
1 1 1 2 2 2 3 3
정답:
1 1 1 3 3 2 2 2

입력:
4
6 7 3 4
정답:
3 6 4 7

입력:
5 
1 3 5 7 9
정답:
1 3 5 7 9



'''
N = int(input())
L = list(map(int,input().split()))
L = sorted(L)
D = dict.fromkeys(L)
K = list(D)
for i in K:
    D[i] = L.count(i)



print(K) 
for i in K:
    num = D[i]
    for j in range(num):
        print(i,end=' ')
