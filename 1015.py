'''
3
A = 2 3 1
비 내림차순 수열 B란?
각각의 원소가 바로 앞의 원소보다 크거나 같을 경우 
    0 1 2 
A = 2 3 1
B = 1 2 3 

B[P[0]] = A[0]
B[p[1]] = A[1]
B[P[2]] = A[2]



B[1] = A[0] 2 
B[2] = A[1] 3
B[0] = A[2] 1  

p[0] = 1 > B.index(A[0])
p[1] = 2
p[2] = 0 



4
A = 2 1 3 1
B = 1 1 2 3

B[P[0]] = 2
B[P[1]] = 1
B[P[2]] = 3
B[P[3]] = 1

P[0] = B[2]
P[1] = B[0]
P[2] = B[3]
P[3] = B[1]



'''
n = int(input())
A = list(map(int,input().split()))

B = sorted(A)
P = [0]*n
for i in range(n):
    
    for j in range(0,len(B)):
        
        if A[i] == B[j]:
            P[i] = j
            B[j] = -1
            break
            
for i in range(len(P)):
    if i == n-1:
        print(P[i])
    else:
        print(P[i],end=" ")