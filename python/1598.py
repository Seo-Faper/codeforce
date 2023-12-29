a,b = map(int,input().split())
if a >= b:
    tmp = a
    a = b
    b = tmp

a -= 1
b -= 1

# a b 의 각 좌표값 구함
a_x = a // 4
a_y = a % 4
b_x = b // 4
b_y = b % 4

result = 0

result += b_x - a_x

if b_y >= a_y:
    result += b_y - a_y
else:
    result += a_y - b_y

print(result)