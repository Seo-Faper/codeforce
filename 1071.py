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
import itertools
N = int(input())
L = list(map(int,input().split()))
L = sorted(L)
for i in itertools.permutations(L):
    print(i)
    flag = True
    D = list(i)
    for j in range(N-1):
        if D[j]+1 == D[j+1]:

            flag = False
            break
    if flag:
        print(*i,end=' ')
        break 
