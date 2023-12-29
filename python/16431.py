B = list(map(int,input().split()))
D = list(map(int,input().split()))
G = list(map(int,input().split()))

Btime = max(abs(G[0] - B[0]) , abs(G[1] - B[1]))
Dtime = abs(G[0] - D[0]) + abs(G[1] - D[1])

if Btime < Dtime : print("bassie") 
elif Btime > Dtime : print("daisy")
else: print("tie")
