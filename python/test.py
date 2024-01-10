n=int(input())
oxquiz=[input() for _ in range(n)]
score=list(0 for k in range(n))
for i in range(n):
    tmp=1
    for j in range(len(oxquiz[i])-1):
        if oxquiz[i][j]=="O":
            score[i] += tmp
            if oxquiz[i][j+1]=="O":
                tmp+=1
            else: tmp=1
        if j==(len(oxquiz[i])-2) and oxquiz[i][j+1]=="O":
            score[i] += tmp
    print(score[i])