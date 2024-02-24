def f0(n):
    if n > 0 and n != 1:
        return True
    return False
def f1(n):
    if n < 0:
        return True
    return False

n = int(input())
l = [int(input()) for _ in range(n)]
zero = l.count(1)
mino = list(filter(f1,l))
plus = list(filter(f0,l))
mino.sort()
plus.sort(reverse=True)
ans = 0
if len(mino) % 2 == 0 :
    for i in range(0,len(mino),2):
        ans += mino[i] * mino[i+1]
else:
    for i in range(0,len(mino)-1,2):
        ans += mino[i] * mino[i+1]
    if not 0 in l: 
        ans += mino[len(mino)-1]

if len(plus) % 2 == 0 :
    if len(plus) == 2:
        ans += max(plus[0]+plus[1],plus[0]*plus[1])
    else: 
        for i in range(0,len(plus),2):
            ans += plus[i] * plus[i+1]
else:
    for i in range(0,len(plus)-1,2):
        ans += plus[i] * plus[i+1]
    ans += plus[len(plus)-1]
ans += zero
print(ans)