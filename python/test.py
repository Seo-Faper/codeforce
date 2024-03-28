a=int(input())
b=list(map(int,input().split()))
num=int(input())
for i in range(num):
    print(b)
    x,y=map(int,input().split())
    if x==1:
        for l in range(1,a//y+1):
            if b[y*l-1]==0:
                b[y*l-1]=1
            elif b[y*l-1]==1:
                b[y*l-1]=0
    else:
        c=[]
        c.append(y-1)
        c.append(a-y)
        c.sort()
        y-=1
        if y==0 or y==(a-1):
            if b[y]==1:
                b[y]=0
                continue
            elif b[y]==0:
                b[y]=1
                continue  
        elif b[(y-c[0])]==b[(y+c[0])]:
                for k in range(y-c[0],y+c[0]+1):
                    if b[k]==1:
                        b[k]=0
                    elif b[k]==0:
                        b[k]=1
                continue
        for l in range(c[0]+1):
            if b[y-l]!=b[y+l]:
                for k in range(y-l-1,y+l,1):
                    if b[k]==1:
                        b[k]=0
                    elif b[k]==0:
                        b[k]=1
                break
    
num=1
for i in range(1,a+1):
    if (i-(20*num))==1:
        print()
    print(b[i-1],end=" ")