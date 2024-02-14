
temp = float(input())
while(True):
    temp2 = float(input())
    if temp2 == 999:
        break
    print(format(temp2 - temp,".2f"))
    temp = temp2