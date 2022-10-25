'''
앞 : H
뒤 : T


'''

n = int(input())
L = [input() for _ in range(n)]
for i in L:
    ans = [0,0,0,0,0,0,0,0]
    w = ''
    for j in range(0,38):
        w = i[j]+i[j+1]+i[j+2]
        if w == 'TTT': ans[0] +=1
        elif w == 'TTH': ans[1] +=1
        elif w == 'THT': ans[2] +=1
        elif w == 'THH': ans[3] +=1
        elif w == 'HTT': ans[4] +=1
        elif w == 'HTH': ans[5] +=1
        elif w == 'HHT': ans[6] +=1
        elif w == 'HHH': ans[7] +=1
            
    print(*ans)
    #뭔데