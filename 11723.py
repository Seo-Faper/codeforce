import sys
N = int(sys.stdin.readline())
S = 0


for i in range(N):

    t = sys.stdin.readline().split()
    a = t[0]
    if a !='all' and a !='empty': b = int(t[1])
    if a=="add":
        S |= (1 << b)
    elif a=="remove":
        S &= ~(1 << b)
    elif a=="check":
        print(1 if S & (1 <<b) != 0 else 0)
    elif a=="toggle":
        S ^= (1 << int(b))
    elif a=="all":
        S = (1 << 21) - 1 
    else:
        S = 0