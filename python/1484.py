N = int(input())
init = 1   
ans = [] 
while True:
    if (init)**2 - (init-1)**2 >= N: break
   # print(init)
    if (N+init**2)**0.5 == int((N+init**2)**0.5): ans.append(int((N+init**2)**0.5))
    init+=1
if ans:
    for x in ans:
        print(x)
else: print(-1)