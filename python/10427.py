def solution(n,A):
    A.sort()
    ans = 0
    s = list.copy(A)
    s.pop()
    for i in range(2,n):
        tmp = 999_999_999
        for j in range(i-2,n-1):

           s[j- (i-2)] += A[j+1]
           #print(i,A[j+1], s[j - (i-2)], A[j+1])
           p = i * A[j+1] - s[j - (i-2)]
           tmp = min(tmp,p)
        
        ans += tmp
    ans += n * A[n-1] - sum(A)
    print(ans)
T = int(input())
for _ in range(T):
    A = list(map(int,input().split()))
    solution(A[0], A[1:])