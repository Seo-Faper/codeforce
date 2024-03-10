a,b = map(int, input().split())
a -= 1
ans_a = a
ans_b = b
for i in range(1,99):
    ans_a += a//(2**i)*(2**(i-1))
for i in range(1,99):
    ans_b += b//(2**i)*(2**(i-1))

print(ans_b-ans_a)