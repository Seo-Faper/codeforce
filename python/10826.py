import sys

a = int(input())
sys.setrecursionlimit(10**6)
def mul(A, B):
    n = len(A)
    Z = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += A[row][i] * B[i][col]
            Z[row][col] = e 
            
    return Z

def square(A, k):
    if k == 1:
        return A
    
    tmp = square(A, k//2)
    if k % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)
    
fib_matrix = [[1, 1], [1, 0]]
if a == 0: print(0)
else:
    print(str(square(fib_matrix, a)[0][1]))