N = int(input())
bird = N
s = 0
l = 0
while True:
    if bird == 0: break
    if bird >= s:
        bird -= s
        s+=1
        l+=1
    else:
        s = 1
print(l-1)