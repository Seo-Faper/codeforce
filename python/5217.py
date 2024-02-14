n = int(input())
for i in range(n):
    num = int(input())
    ans = "Pairs for "+str(num)+": "
    p = []
    for j in range(1,num//2+1):
        for k in range(1,num+1):
            if j != k and j + k == num:
                p.append(str(j)+" "+str(k))

                break         
    ans += ', '.join(p)
    print(ans)