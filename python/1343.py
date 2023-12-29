s = input()
count = 0
c = 0
f = False
for i in s:
    if i == 'X':
        c+=1
    else:
        if c % 2 !=0:
            f = True
            break
if c %2 !=0: f = True
if f:
    print(-1)
else:
    for i in s:
        if i == 'X':
            count +=1
        else:
            A = count//4
            B = count%4
            print("A"*A*4+"B"*B,end='')
            count = 0
        if count == 0:
            print(i,end='')
    if count != 0:
        A = count//4
        B = count%4
        print("A"*A*4+"B"*B,end='')
