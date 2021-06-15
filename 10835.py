def f(left,right):
    if left >=n or right >=n: return 0
    result = 0 
    if L[left] > R[right] : result += R[right] + f(left,right+1)
    else:
        result +=max(f(left+1,right),f(left+1,right+1))
    return result

n = int(input())
L = list(map(int,input().split()))
R = list(map(int,input().split()))
print(f(0,0))
