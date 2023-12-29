


W, H, X, Y, P = map(int,input().split())

def f(x,y):
    # 사각형 안에 있는 지
    if X <= x <= X + W and Y <= y <= Y+ H: return True

    # 왼쪽 반원 안에 있는지 
    if (x-X)**2 + (y-(H/2+Y))**2 <= (H/2)**2: return True

    # 오른쪽 반원 안에 있는지
    if (x-(X+W))**2 + (y-(H/2+Y))**2 <= (H/2)**2: return True

    return False

ans  = 0
for i in range(P):
    x,y = map(int,input().split())
    if f(x,y): ans +=1
print(ans)
