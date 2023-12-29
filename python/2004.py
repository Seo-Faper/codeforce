def five_count(n):
    cnt = 0
    while n != 0:
        n //= 5
        cnt += n
    return cnt

def two_count(n):
    cnt = 0
    while n != 0:
        n //= 2
        cnt += n
    return cnt

N,M = map(int, input().split())


A = five_count(N),two_count(N)

B = five_count(M),two_count(M)

C = five_count(N-M),two_count(N-M)

print(min(A[0]-(B[0]+C[0]),A[1]-(B[1]+C[1])))

'''
f1_tmp = 0 # 분자)5의 개수
t1_tmp = 0 # 분자) 2의 개수

for i in range(max(M+1,(M-N)+1),N+1):
    print(i,end=' ')

    if i % 5 == 0 : f1_tmp +=1
    if i % 2 == 0 : t1_tmp +=1 

f2_tmp = 0 # 분모)5의 개수
t2_tmp = 0 # 분모) 2의 개수

for i in range(1, max(M+1,(M-N)+1)):
    print(i,end=' ')

    if i % 5 == 0 : f2_tmp +=1
    if i % 2 == 0 : t2_tmp +=1 
'''