N, m, M, T, R = map(int,input().split())

A = 0 # 운동 시간
B = 0 # 휴식 시간
X = m
while True:
    if (M-m<T):
        A = 0
        B = -1
        break
    if A == N : break
    if X+T <= M:
        X+=T
        A += 1 
    elif  X - R < m : 
        X = m
        B+=1
    else: 
        X = X-R
        B+=1

print(A+B)