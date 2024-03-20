def recur(idx, N, current=[]):
    global count
    if idx==N:
        count+=1
        if count == n:
            print(int(''.join(map(str,current))))
        
        return
    for i in range(0,10):
        if current and current[-1] <= i:continue
        recur(idx+1, N, current+[i])

n = int(input())
count = 0
if n < 1024:
    for i in range(1,11):
        recur(0,i)
else:
    print(-1)