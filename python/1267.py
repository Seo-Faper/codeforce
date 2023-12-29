N = int(input())
L = list(map(int,input().split()))

M = 0
Y = 0
# M : 30초에 10원
# Y : 60초에 15원 
for i in L:
    Y +=(i // 30 + 1)*10
    M +=(i //60 + 1)*15

   # print(M,Y)
if Y < M:
    print("Y",Y)
elif Y > M:
    print("M",M)
else:
    print("Y M",Y)