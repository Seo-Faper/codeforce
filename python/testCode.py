l = [2, 1, 1, 2, 3, 1, 2, 3, 1]	
sk = []
burger = "1231"
ans = 0
for i in l:
    sk.append(i)
    # print(sk,''.join(map(str,sk[-4:])), burger)
    if len(sk)>=4 and ''.join(map(str,sk[-4:])) == burger:
       ans +=1
       sk.pop()
       sk.pop()
       sk.pop()
       sk.pop()
print(ans)
