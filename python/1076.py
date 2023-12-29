table = {"black":1,
        "brown":10,
        "red":100,
"orange":1000,
"yellow":10000,
"green":100000,
"blue":1000000,
"violet":10000000,
"grey":100000000,
"white":1000000000}

ans = ""
l = [input()for i in range(3) ]

for p in enumerate(table):
    if p[1] == l[0]: ans += str(p[0])

for p in enumerate(table):
    if p[1] == l[1]: ans+=str(p[0]) 

for p in enumerate(table):
    if p[1] == l[2]: print (table[l[2]]*int(ans))