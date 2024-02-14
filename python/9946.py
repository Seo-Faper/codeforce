n = 1
while True:
    a = input()
    b = input()
    if a == "END": break
    ax = ''.join(sorted(list(a)))
    bx = ''.join(sorted(list(b)))
    if ax != bx: print("Case "+str(n)+": different")
    else : print("Case "+str(n)+": same")
    n+=1