S = input()
sk = []
ans = 0
for i in S:
    if i =='(':
        sk.append(i)
    else:
        sk.pop()
        ans +=len(sk)
        print(sk)
print(ans)