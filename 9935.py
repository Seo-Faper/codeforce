S = input()
k = input()

size = len(k)
last = k[-1]

ans = ""
sk = []
for i in S:
    sk.append(i)
    
    if sk[-1] == last and "".join(sk[-size:]) == k:
        for i in range(size):
            sk.pop()

if sk:
    for i in sk:
        print(i,end='')
else:
    print("FRULA")