n = int(input())
for i in range(n):
    N,C = map(int, input().split())
    if N%C==0:
        print(N//C )
    else: print(N//C + 1 )