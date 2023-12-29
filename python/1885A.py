N = int(input())
while True:
    if N == 0: break
    p = int(input())
    l = [int(x) for x in input().split()]
   #print(l)
    ans = 0
    for i in range(p):
        #print(l[i],end=' ')
        if l[i] == i+1:
           ans+=1 
    print(ans//2 + ans % 2)
    N-=1