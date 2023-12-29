
M = int(input())
N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]

s = 0
for i in L:
    s +=(i[0]*i[1])
#print(M,s)

if M==s: print("Yes")
else: print("No")