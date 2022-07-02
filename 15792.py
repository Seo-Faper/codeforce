a,b = map(int,input().split())
print( a//b ,end='.')
for i in range(1100):
    t = (a % b)*10
    print(t // b,end='')
    a = t % b
