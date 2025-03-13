T = int(input())
for _ in range(T):
    s = input()
    n = (len(s)+2)//3
    sp = s[0:n]
    rev = sp[::-1]
    tail = sp[1::]

   
    if s == sp + rev + sp or s == sp + sp[::-1][1::] + sp or s == sp + rev + tail or s ==  sp + sp[::-1][1::] + tail:
        print(1)
    else:
        print(0)