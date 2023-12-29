
def solve(a,b,np,p):
    count = 0
    while(np):
        if max(p) > np[0][0]:
            np.append(np.pop(0))
        else:
            count+=1
            if np.pop(0)[1] == b:
                return count
            p.remove(max(p))


T = int(input())
ans = []
np = []
for i in range(T):
    a,b = map(int, input().split())
    priority = list(map(int,input().split()))
    for j in range(a):
        np.append([priority[j],j])
    ans.append(solve(a, b, np,priority))

for i in ans:
    print(i)