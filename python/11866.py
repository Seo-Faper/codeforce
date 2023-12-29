n,k = map(int, input().split())

queue = []
for i in range(1,n+1):
    queue.append(i)

tmp = 1
ans = []
while(queue):
    if tmp == k:
       ans.append(queue.pop(0))
       tmp = 1
    else:
        queue.append(queue.pop(0))
        tmp+=1 

print("<",end = '')
for i in range(len(ans)):
    if i != len(ans)-1: print(ans[i],end = ', ')
    else: print(ans[i],end = '')

print(">")