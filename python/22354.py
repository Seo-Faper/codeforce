'''
8
WBBWBWBB
6 4 8 2 5 3 1 5

9
WBBBWBWBB
6 10 4 9 2 5 3 1 5


B W B  W B W
1 9 10 1 2 2 



 ( N-2 ) / 2 번 가장 큰 수를 가져옴

[6 8 2 5 3 5]

양 옆 제외 [8 2 5 3] / 2 개 



'''
result = []
def solution(stone,L, n):
    L[0] = 0
    L[-1] = 0
    i = 0
    R = []
    P = ""
    M = 0
    M_index = 0
    while(i < n):
        S = []
        K = []
        ff = 0
        for j in range(i,n):
            if stone[i] == stone[j]:
                S.append(L[j])
                ff = max(L[j],ff)
                K.append(stone[j])   
            else:
                break
    #print(max(S))
    #print(K)
        i+=len(S)
        P +=K[0]
        
        R.append(ff)
        if ff > M and 0 < i < n-1:
            M = ff
            M_index = len(R)-1


    #print(M,M_index)
    R.pop(M_index)
    t = list(P)
    t[M_index] = ""
    P = "".join(t)
  #  print(R)
   # print(P)
    result.append(M)
    return [P,R]
n = int(input())
stone = input()
L = list(map(int, input().split()))


#print(L)
for i in range((n-2)//2):
   # print(stone,L)
    r = solution(stone, L, n)
    stone = r[0]
    L = r[1]
    n = len(L)

print(sum(result))