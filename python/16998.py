import sys
input = sys.stdin.readline
T = int(input().rstrip())
def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p

def calculate(p, q, n):
    G = gcd(p, q)
    P = p // G
    result = 0

    mod_values = [(P * i) % q for i in range(1, q+1)]

    result = sum(mod_values[:n % q]) + sum(mod_values) * (n // q)

    final_result = (G * result) 
    
    return final_result
for _ in range(T):
    p,q,n = map(int, input().rstrip().split())
    ans = calculate(p,q,n)
    sys.stdout.write(str(ans)+"\n")