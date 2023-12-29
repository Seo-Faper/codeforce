N = int(input())
ans = []
for i in range(N):
    k = list(map(int,input().split()))
    l = set(k)
    if len(list(l)) == 1: ans.append(10000+k[0]*1000)
    elif len(list(l))==2: 
        if k[0] == k[1]: ans.append(1000+k[0]*100)
        elif k[1]==k[2]: ans.append(1000+k[1]*100)
        else: ans.append(1000+k[0]*100)
    else:
        ans.append(max(k)*100)

print(max(ans))