import sys

input = sys.stdin.readline
print = sys.stdout.write
def up(P, K):
    P_list = list(P)
    

        
    if int(P_list[K]) >= 5:
  
        for i in range(K,len(P)):
            P_list[i] = '0'

        if K == 0:
            P_list.insert(0,'1')
       
        else:
            P_list[K - 1] = str(int(P_list[K - 1]) + 1)
    return ''.join(P_list)

N = int(input())
for i in range(N):
    p = input()
    ans = 0
    f = False
    for j in range(len(p)):
        p = up(p, j)
        if int(p) < ans:
            f = True
            break
        ans = max(int(p),ans)   
    if f:
        print(str(ans))
        break
    for j in reversed(range(len(p))):
        p = up(p, j)
        if int(p) < ans:
            break
        ans = max(int(p),ans)
    print(str(ans))