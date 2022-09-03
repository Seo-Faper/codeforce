N = input()
ans  = 1
s = ""
while True:
    s+=str(ans)
    if s[len(s)-len(N):] == N: 
        print(s.index(N)+1)
        break
    ans +=1
