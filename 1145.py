L = list(map(int,input().split()))
ans = 1
while True:
    count = 0

    for i in L:
        # print(ans % i)
        if ans % i == 0: count+=1
    ans +=1
   # print("count : "+str(count)+" ans : "+str(ans))
    if count >= 3: break

print(ans-1)