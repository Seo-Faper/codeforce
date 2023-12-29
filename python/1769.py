n = input()
ans =1
if int(n) < 10:
    print(0)
    if int(n)%3==0: print("YES")
    else: print("NO")
else:

    while True:
        Y = sum(list(map(int,n)))
        n = str(Y)    
        if Y < 10:
            break
        ans+=1

    print(ans)
    if Y ==3 or Y==6 or Y==9: print("YES")
    else: print("NO")
    