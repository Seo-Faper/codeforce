N = int(input())
l = []
a = [0]*N
for i in range(N):
    e = int(input())
    a[e]+=1

print(a)
for i in reversed(range(N)):
    if a[i] !=0:
        print(a[i])
