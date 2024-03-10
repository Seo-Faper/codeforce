a=int(input())
cow=[input() for _ in range(a)]
cow.sort()
print(cow)
time=0
for i in range(a):
    b,c=cow[i].split()
    if time<=int(b):
        time=int(b)+int(c)
    else: time+=int(c)
print(time)