
N,r,c = map(int,input().split())

def f(N,r,c):
    if N == 0:
        return 0
    else:
        return 2*(r%2)+(c%2) + 4 * f(N-1, r//2, c//2)
print(f(N,r,c))