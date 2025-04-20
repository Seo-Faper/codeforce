"""
12345 

12346

12 46

46이 12보다 크기 때문에 46앞의 자리를 +1 해준다.
그럼 12400이 되고, 여기서 부터 1씩 증가시켜주면 12421이 된다. 그럼 N보다 큰 팰린드롬수가 된다.

9999를 예로 들면
10000이 되고 left = 10, right = 00이 된다. 10이 00보다 크기 때문에 right에 1을 더해준다.
그럼 10001이 된다.

12345 -> 12346 -> 12421
1999 -> 2000 -> 2002
123 -> 124 -> 131
191 -> 192 -> 202
1234 -> 1235 -> 1241
"""

s = int(input())
s+=1

temp =str(s)
if len(temp) == 1:
    print(s)
    exit()

if len(temp)%2 == 0:
    left = temp[:len(temp)//2]
    right = temp[len(temp)//2:]
    if int(left[::-1]) < int(right):
        left = str(int(left)+1)
    right = left[::-1]
    
else:
    left = temp[:len(temp)//2]
    mid = temp[len(temp)//2]
    right = temp[len(temp)//2+1:]
    if int(left[::-1]) < int(right): # left를 reverse한 값이 right보다 작으면 mid를 +1 해줘야함
        if int(mid) == 9: # 9가 들어오면 left를 +1 해줘야함
            left = str(int(left)+1)
            mid = '0'
        else:
            mid = str(int(mid)+1)
    right = mid+left[::-1]
        
print(left+right)

