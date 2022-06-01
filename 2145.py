def f(k):
    tmp = 0
    for i in k:
        tmp += int(i)
    return str(tmp)
while True:
    s = input()
    if s == '0': break
    while True:
        if len(s) == 1: 
            print(s)
            break
        s = f(s)     