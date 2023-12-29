# 456789101112131415161718192021
n = input()

A = 0
B = 0
flag = False
for i in range(1,len(n)+1):
    if flag: break
    T = int(n[:i])
    B = 0
    s = ""
    A = T
    s+=str(A)
    while True:
        if s == n:
            
            print(T,T+B)   
            flag = True
            break

        if s != n[:len(s)]: break
        A+=1
        s+=str(A)
        #print(s,n[:len(s)])
        B+=1
