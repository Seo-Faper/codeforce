S = input()
T = input()
while True:
    if S == T : 
        print(1)
        break
    if T[-1:]=='A':
        T = T[:-1]
    elif T[-1:]=='B':
        T = T[:-1]
        T = T[::-1]
    else:
        print(0)
        break