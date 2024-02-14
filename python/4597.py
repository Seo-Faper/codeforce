while True:
    s = input()
    mod = ''
    a = '0'
    b = '1'
    if s =="#": break
    if s[len(s)-1] == 'e':
        mod = 'e'

    else:
        mod = 'o'
        a = '1'
        b = '0'
    if s.count('1') % 2 == 0:
        s = s.replace(mod,a)
    else:
        s = s.replace(mod,b)
    print(s)
