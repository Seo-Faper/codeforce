n = int(input())
l = list(int(input()) for _ in range(n))
for i in l:
    print(i//5*"++++ "+i%5*"|")