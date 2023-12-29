a0 = list(input())
b0 = list(input())
L = [0]*26
R = [0]*26
for i in a0:
    L[ord(i)-97] +=1

for i in b0:
    R[ord(i)-97] +=1

#print(L)
#print(R)
ans = 0
for i in range(26):
    ans+= abs(L[i]-R[i])

print(ans)