n = int(input())
for _ in range(n):
    a,d = input().split()
    if d == 'kg':
        print("{:.4f} lb".format(round(float(a)*2.2046,4)))
    if d == 'lb':
        print("{:.4f} kg".format(round(float(a)*0.4536 ,4)))
    if d == 'g':
        print("{:.4f} l".format(round(float(a)*	3.7854,4)))
    if d == 'l':
        print("{:.4f} g".format(round(float(a)*0.2642,4)))