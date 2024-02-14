T= int(input())

for i in range(T):
    temp=[]
    n = int(input())
    for j in range(1,n//2+1):
        for k in range(1,n+1):
                if k!=j and k+j==n:
                    temp.append(str(j)+" "+str(k))
                    break
    if temp:
        print(f"Pairs for {n}: {', '.join(temp)}")
        
    else:
        print(f"Pairs for {n}:")