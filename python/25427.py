N = int(input())
S = input()
dir = "DKSH"
d = 0
k = 0
s = 0
h = 0
for i in range(len(S)):
    if S[i] == 'D':
        d+=1
        continue
    if S[i] == 'K':
        k+=d
        continue
    if S[i] =='S':
        s +=k
    if S[i]=='H':
        h+=s
print(h)