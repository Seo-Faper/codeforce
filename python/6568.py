PC = 0
calc = 0
mem = {}
for _ in range(32):
    i = input()
    cmd = int(i[0:3],2)
    value = i[3:8]
    if cmd == 0:
        mem[value] = calc
    elif cmd == 1:
         calc = mem[value]
    elif cmd == 2:
        if calc == 0:
            PC = int(value,2)
    elif cmd == 4:
        calc+=1
    elif cmd == 5:
        calc = max(0, calc-1)
    elif cmd == 6:
        PC = int(value,2)
    elif cmd ==1:
        break