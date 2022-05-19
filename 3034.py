import math
N,W,H = map(int, input().split())
for i in range(N):
    a = int(input())
    if math.sqrt((W**2 + H**2)) >= a:
        print("DA")
    else:
        print("NE")