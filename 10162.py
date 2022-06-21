# 100
    
# 0 1 4
# 100초를 만드는데 
# 
# 1분 40초
n = int(input())

S = [300,60,10]
if str(n)[len(str(n))-1]=='0':
    a = n//S[0]
    b = n%S[0] // S[1]
    c = n%S[1] // S[2]
    print(a,b,c)
else:
    print(-1)