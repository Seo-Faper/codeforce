import math
def conv(e):
    temp_s = e
    while len(temp_s) != size:
        temp_s += e
    return temp_s
s = input()
t = input()
size = math.lcm(len(s),len(t))
#print(size)
if conv(s) == conv(t):
    print(1)
else:
    print(0)